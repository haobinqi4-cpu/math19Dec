#!/usr/bin/env python3
"""
Test script to verify HKBU Gen AI API connectivity
Helps diagnose API key and endpoint issues
"""

import requests
import json
from pathlib import Path

# Configuration
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR.parent / "Data"
API_KEY_FILE = DATA_DIR / "GenAIkey.md"
API_BASE_URL = "https://genai.hkbu.edu.hk/api/v0/rest"

def load_api_key():
    """Load API key from file"""
    if not API_KEY_FILE.exists():
        print(f"❌ API key file not found: {API_KEY_FILE}")
        return None
    
    try:
        with open(API_KEY_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            # Remove markdown code blocks if present
            if content.startswith('```'):
                lines = content.split('\n')
                content = '\n'.join(lines[1:-1]).strip()
            return content.strip()
    except Exception as e:
        print(f"❌ Error reading API key: {e}")
        return None

def test_list_models(api_key):
    """Test listing available models"""
    print("\n1️⃣ Testing: List Available Models")
    print(f"   URL: {API_BASE_URL}/models")
    
    try:
        response = requests.get(
            f"{API_BASE_URL}/models",
            headers={"api-key": api_key},
            timeout=10
        )
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            models = data.get('data', [])
            print(f"   ✅ Success! Found {len(models)} models")
            if models:
                print(f"   Sample models: {', '.join([m.get('id', '?') for m in models[:5]])}")
            return True
        else:
            print(f"   ❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def test_chat_completion(api_key, model="gpt-5", endpoint_format="standard"):
    """Test chat completion with different endpoint formats"""
    print(f"\n2️⃣ Testing: Chat Completion ({endpoint_format} endpoint)")
    
    if endpoint_format == "standard":
        url = f"{API_BASE_URL}/deployments/{model}/chat/completions"
    else:
        url = f"{API_BASE_URL}/openai/deployments/{model}/chat/completions"
    
    print(f"   URL: {url}")
    print(f"   Model: {model}")
    
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [
            {"role": "user", "content": "Say 'Hello, world!' if you can read this."}
        ],
        "max_tokens": 50,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            content = data.get('choices', [{}])[0].get('message', {}).get('content', '')
            print(f"   ✅ Success! Response: {content[:100]}")
            return True
        else:
            error_data = response.json() if response.content else {}
            error_msg = error_data.get('message', response.text)
            print(f"   ❌ Failed: {error_msg}")
            if response.status_code == 401:
                print(f"   ⚠️  This suggests your API key may be invalid or expired")
            return False
    except requests.exceptions.Timeout:
        print(f"   ❌ Timeout - API server may be slow or unreachable")
        return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("🧪 HKBU Gen AI API Connection Test")
    print("=" * 60)
    
    # Load API key
    api_key = load_api_key()
    if not api_key:
        print("\n❌ Cannot proceed without API key")
        print(f"   Please ensure your API key is in: {API_KEY_FILE}")
        return 1
    
    print(f"\n✅ API Key loaded (length: {len(api_key)}, starts with: {api_key[:8]}...)")
    
    # Test 1: List models
    models_ok = test_list_models(api_key)
    
    # Test 2: Chat completion (standard endpoint)
    chat1_ok = test_chat_completion(api_key, "gpt-5", "standard")
    
    # Test 3: Chat completion (alternative endpoint)
    if not chat1_ok:
        print("\n   Trying alternative endpoint format...")
        chat2_ok = test_chat_completion(api_key, "gpt-5", "openai")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    if models_ok and (chat1_ok or chat2_ok):
        print("✅ API connection is working!")
        print("   Your chatbot should function correctly.")
        return 0
    elif not models_ok:
        print("❌ Cannot list models - API key may be invalid")
        print("   Please check:")
        print("   1. Your API key is correct")
        print("   2. Your API key has not expired")
        print("   3. You have access to HKBU Gen AI Platform")
        return 1
    else:
        print("⚠️  Partial success - some features may not work")
        print("   Chat completion failed but model listing works")
        return 1

if __name__ == '__main__':
    exit(main())

