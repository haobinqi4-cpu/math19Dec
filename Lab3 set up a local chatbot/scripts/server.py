#!/usr/bin/env python3
"""
Local Chatbot Server for HKBU Gen AI Platform
Provides a Flask backend to handle LLM API calls and file management
"""

import os
import json
import requests
from datetime import datetime
from pathlib import Path
from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS

app = Flask(__name__, static_folder='..', static_url_path='')
CORS(app)

# Configuration
BASE_DIR = Path(__file__).parent.parent  # Lab3 set up a local chatbot/
WORKSPACE_ROOT = BASE_DIR.parent          # math19Dec/
DATA_DIR = WORKSPACE_ROOT / "Data"        # math19Dec/Data/
CHAT_HISTORY_DIR = BASE_DIR / "chatHistory"

# Load API keys from files
HKBU_API_KEY_FILE = DATA_DIR / "GenAIkey.md"
KIMI_API_KEY_FILE = DATA_DIR / "Kimi.md"

HKBU_API_KEY = None
KIMI_API_KEY = None

# Load HKBU Gen AI API key
if HKBU_API_KEY_FILE.exists():
    try:
        with open(HKBU_API_KEY_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content.startswith('```'):
                lines = content.split('\n')
                content = '\n'.join(lines[1:-1]).strip()
            HKBU_API_KEY = content.strip()
            if HKBU_API_KEY:
                print(f"[INFO] HKBU API Key loaded (length: {len(HKBU_API_KEY)}, starts with: {HKBU_API_KEY[:8]}...)")
    except Exception as e:
        print(f"[ERROR] Failed to load HKBU API key: {e}")

# Load Kimi API key
if KIMI_API_KEY_FILE.exists():
    try:
        with open(KIMI_API_KEY_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content.startswith('```'):
                lines = content.split('\n')
                content = '\n'.join(lines[1:-1]).strip()
            # Take first line only (in case there are extra blank lines)
            KIMI_API_KEY = content.split('\n')[0].strip()
            # Remove all whitespace to be safe
            KIMI_API_KEY = ''.join(KIMI_API_KEY.split())
            if KIMI_API_KEY:
                print(f"[INFO] Kimi API Key loaded (length: {len(KIMI_API_KEY)}, starts with: {KIMI_API_KEY[:8]}...)")
    except Exception as e:
        print(f"[ERROR] Failed to load Kimi API key: {e}")

# Use Kimi API key as primary if available, otherwise fallback to HKBU
API_KEY = KIMI_API_KEY if KIMI_API_KEY else HKBU_API_KEY
USE_KIMI = bool(KIMI_API_KEY)

# API Configuration
HKBU_API_BASE_URL = "https://genai.hkbu.edu.hk/api/v0/rest"
KIMI_API_BASE_URL = "https://api.moonshot.cn/v1"

# Set active API
if USE_KIMI:
    API_BASE_URL = KIMI_API_BASE_URL
    print(f"[INFO] Using Kimi (Moonshot AI) API")
else:
    API_BASE_URL = HKBU_API_BASE_URL
    print(f"[INFO] Using HKBU Gen AI API")

# Available models - Kimi (Moonshot AI) models
# Common working models based on API availability
KIMI_MODELS = [
    {"id": "moonshot-v1-8k", "name": "Moonshot v1 8K", "provider": "Moonshot AI"},
    {"id": "moonshot-v1-32k", "name": "Moonshot v1 32K", "provider": "Moonshot AI"},
    {"id": "moonshot-v1-128k", "name": "Moonshot v1 128K", "provider": "Moonshot AI"},
    {"id": "moonshot-v1-auto", "name": "Moonshot v1 Auto (128K)", "provider": "Moonshot AI"},
    {"id": "kimi-latest", "name": "Kimi Latest (128K)", "provider": "Moonshot AI"},
]

# Available models - HKBU Gen AI models
HKBU_MODELS = [
    {"id": "gpt-5", "name": "GPT-5", "provider": "OpenAI"},
    {"id": "gpt-5-mini", "name": "GPT-5 Mini", "provider": "OpenAI"},
    {"id": "gpt-4.1", "name": "GPT-4.1", "provider": "OpenAI"},
    {"id": "gpt-4.1-mini", "name": "GPT-4.1 Mini", "provider": "OpenAI"},
    {"id": "o1", "name": "O1 (Reasoning)", "provider": "OpenAI"},
    {"id": "o3-mini", "name": "O3-Mini", "provider": "OpenAI"},
    {"id": "gemini-2.5-pro", "name": "Gemini 2.5 Pro", "provider": "Google"},
    {"id": "gemini-2.5-flash", "name": "Gemini 2.5 Flash", "provider": "Google"},
    {"id": "llama-4-maverick", "name": "Llama 4 Maverick", "provider": "Meta"},
    {"id": "qwen3-max", "name": "Qwen 3 Max", "provider": "Alibaba"},
    {"id": "qwen-plus", "name": "Qwen Plus", "provider": "Alibaba"},
    {"id": "deepseek-r1", "name": "DeepSeek R1", "provider": "DeepSeek"},
    {"id": "deepseek-v3", "name": "DeepSeek V3", "provider": "DeepSeek"},
]

# Set active models based on API
MODELS = KIMI_MODELS if USE_KIMI else HKBU_MODELS

@app.route('/')
def index():
    """Serve the main HTML page"""
    return app.send_static_file('chatbot.html')

@app.route('/favicon.ico')
def favicon():
    """Serve favicon"""
    return app.send_static_file('favicon.svg')

@app.route('/api/models', methods=['GET'])
def get_models():
    """Return list of available models"""
    return jsonify({"models": MODELS})

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat completion requests"""
    if not API_KEY:
        return jsonify({"error": "API key not found. Please check GenAIkey.md or Kimi.md"}), 500
    
    data = request.json
    model = data.get('model', MODELS[0]['id'] if MODELS else 'moonshot-v1-32k').strip()  # Remove any whitespace
    messages = data.get('messages', [])
    stream = data.get('stream', False)
    max_tokens = data.get('max_tokens', 2000)
    temperature = data.get('temperature', 0.7)
    
    # Build the API request based on which API we're using
    if USE_KIMI:
        # Kimi (Moonshot AI) API format
        url = f"{API_BASE_URL}/chat/completions"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
    else:
        # HKBU Gen AI API format - try both endpoint formats
        url1 = f"{HKBU_API_BASE_URL}/deployments/{model}/chat/completions"
        url2 = f"{HKBU_API_BASE_URL}/openai/deployments/{model}/chat/completions"
        url = url1  # Will try url2 as fallback
        headers = {
            "api-key": API_KEY,
            "Content-Type": "application/json"
        }
    
    # Build payload - ensure model is included for Kimi API
    if USE_KIMI:
        payload = {
            "model": model,  # Kimi API requires model in payload
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
    else:
        payload = {
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": stream
        }
    
    try:
        if stream:
            # Handle streaming response
            def generate():
                if USE_KIMI:
                    try:
                        response = requests.post(url, headers=headers, json=payload, stream=True, timeout=60)
                        if response.status_code == 200:
                            for line in response.iter_lines():
                                if line:
                                    decoded_line = line.decode('utf-8')
                                    if decoded_line.startswith('data: '):
                                        yield decoded_line + '\n\n'
                            return
                    except Exception as e:
                        yield f'data: {{"error": "Kimi API streaming failed: {str(e)}"}}\n\n'
                else:
                    # HKBU API streaming
                    for endpoint_url in [url1, url2]:
                        try:
                            response = requests.post(endpoint_url, headers=headers, json=payload, stream=True, timeout=30)
                            if response.status_code == 200:
                                for line in response.iter_lines():
                                    if line:
                                        decoded_line = line.decode('utf-8')
                                        if decoded_line.startswith('data: '):
                                            yield decoded_line + '\n\n'
                                return
                        except:
                            continue
                    yield 'data: {"error": "Failed to connect to API"}\n\n'
            
            return Response(stream_with_context(generate()), mimetype='text/event-stream')
        else:
            # Handle non-streaming response
            if USE_KIMI:
                # Kimi API - single endpoint
                try:
                    print(f"[DEBUG] Sending request to Kimi API: {url}")
                    print(f"[DEBUG] Model: '{model}' (length: {len(model)})")
                    print(f"[DEBUG] Payload: {json.dumps(payload, indent=2)}")
                    print(f"[DEBUG] API Key length: {len(API_KEY)}, starts with: {API_KEY[:10]}...")
                    response = requests.post(url, headers=headers, json=payload, timeout=60)
                    print(f"[DEBUG] Response status: {response.status_code}")
                    print(f"[DEBUG] Response text: {response.text[:200]}")
                    
                    response.raise_for_status()  # Raise exception for bad status codes
                    return jsonify(response.json())
                except requests.exceptions.RequestException as e:
                    error_msg = str(e)
                    if hasattr(e, 'response') and e.response is not None:
                        error_msg = e.response.text
                    return jsonify({"error": f"Kimi API request failed: {error_msg}"}), 500
            else:
                # HKBU Gen AI API - try both endpoint formats
                for endpoint_url in [url1, url2]:
                    try:
                        print(f"[DEBUG] Trying endpoint: {endpoint_url}")
                        response = requests.post(endpoint_url, headers=headers, json=payload, timeout=30)
                        print(f"[DEBUG] Response status: {response.status_code}")
                        
                        if response.status_code == 200:
                            return jsonify(response.json())
                        elif response.status_code == 401:
                            # Invalid API key - don't try second endpoint
                            error_data = response.json() if response.content else {"error": "Invalid API key"}
                            return jsonify({"error": f"API authentication failed: {error_data.get('message', 'Invalid API key')}"}), 401
                        # For other errors, try next endpoint
                    except requests.exceptions.Timeout:
                        continue
                    except requests.exceptions.RequestException as e:
                        # If first URL fails, try second
                        if endpoint_url == url1:
                            continue
                        raise
                
                # If both URLs failed, return error
                return jsonify({"error": "All endpoint attempts failed"}), 500
    
    except requests.exceptions.RequestException as e:
        error_msg = str(e)
        if hasattr(e, 'response') and e.response is not None:
            error_msg = e.response.text
            print(f"[ERROR] API Error: {error_msg}")
        return jsonify({"error": f"API request failed: {error_msg}"}), 500

@app.route('/api/chat/save', methods=['POST'])
def save_chat():
    """Save chat history to file"""
    data = request.json
    session_name = data.get('session_name', datetime.now().strftime('%Y%m%d_%H%M%S'))
    messages = data.get('messages', [])
    model = data.get('model', 'unknown')
    system_prompt = data.get('system_prompt', '')
    files = data.get('files', [])
    
    # Create chat history file
    filename = f"{session_name}.json"
    filepath = CHAT_HISTORY_DIR / filename
    
    chat_data = {
        "timestamp": datetime.now().isoformat(),
        "session_name": session_name,
        "model": model,
        "system_prompt": system_prompt,
        "files": files,
        "messages": messages
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(chat_data, f, indent=2, ensure_ascii=False)
    
    return jsonify({"success": True, "filename": filename})

@app.route('/api/chat/list', methods=['GET'])
def list_chats():
    """List all saved chat sessions"""
    chat_files = []
    for filepath in CHAT_HISTORY_DIR.glob('*.json'):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                chat_files.append({
                    "filename": filepath.name,
                    "session_name": data.get('session_name', filepath.stem),
                    "timestamp": data.get('timestamp', ''),
                    "model": data.get('model', ''),
                    "message_count": len(data.get('messages', []))
                })
        except:
            pass
    
    # Sort by timestamp, newest first
    chat_files.sort(key=lambda x: x['timestamp'], reverse=True)
    return jsonify({"chats": chat_files})

@app.route('/api/chat/load/<filename>', methods=['GET'])
def load_chat(filename):
    """Load a saved chat session"""
    filepath = CHAT_HISTORY_DIR / filename
    if not filepath.exists():
        return jsonify({"error": "Chat session not found"}), 404
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return jsonify(data)

if __name__ == '__main__':
    # Ensure directories exist
    CHAT_HISTORY_DIR.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("🤖 Local Chatbot Server Starting...")
    print("=" * 60)
    print(f"📁 Base directory: {BASE_DIR}")
    print(f"💾 Chat history: {CHAT_HISTORY_DIR}")
    if USE_KIMI:
        print(f"🔑 API: Kimi (Moonshot AI)")
        print(f"🔑 API Key loaded: {'✓' if KIMI_API_KEY else '✗'}")
        print(f"📋 Models available: {len(KIMI_MODELS)} Kimi models")
    else:
        print(f"🔑 API: HKBU Gen AI")
        print(f"🔑 API Key loaded: {'✓' if HKBU_API_KEY else '✗'}")
        print(f"📋 Models available: {len(HKBU_MODELS)} HKBU models")
    print(f"🌐 Server URL: http://localhost:5000")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
