# Local Chatbot - Quick Start Guide

## For AI Agents: Starting the Server

### 1. Navigate to Lab3 Directory
```bash
cd "/Users/simonwang/Documents/Usage/MathAI/math19Dec/Lab3 set up a local chatbot"
```

### 2. Start the Server
```bash
python3 scripts/server.py
```

### 3. Verify Server is Running
- Server starts on: `http://localhost:5000`
- Check status: `curl http://localhost:5000/api/models`
- Expected: JSON response with available models

### 4. Stop Server (if needed)
```bash
pkill -f "scripts/server.py"
```

---

## For Users: Using the Chatbot

### Access the Chatbot

1. **Open your web browser**
2. **Navigate to:** `http://localhost:5000`
3. **You're ready to chat!**

### How to Use

#### 1. Select a Model
- Choose from dropdown in the left sidebar
- Available models: moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k, moonshot-v1-auto, kimi-latest

#### 2. Set System Prompt (Optional)
- Define the AI's role and behavior
- Example: "You are a helpful math tutor for MSc students."

#### 3. Add File Context (Optional)
- Enter filename
- Paste file content
- Click "📎 Add File"
- Files are included in every message

#### 4. Start Chatting
- Type your message in the input box
- Press Enter or click Send
- Wait for AI response

#### 5. Save/Load Conversations
- **Save**: Click "💾 Save" button, enter session name
- **Load**: Click "📂 Load" to view and restore saved chats
- **Clear**: Click "🗑️ Clear" to start fresh

---

## Quick Troubleshooting

### Server Won't Start?
```bash
# Install dependencies
pip install flask flask-cors requests

# Check if port 5000 is in use
lsof -i :5000
```

### Can't Connect?
- Ensure server is running (check terminal)
- Try: `http://127.0.0.1:5000` instead of `localhost:5000`
- Check firewall settings

### API Errors?
- Verify API key exists: `../Data/Kimi.md`
- Server automatically uses Kimi API if `Kimi.md` exists
- Otherwise uses HKBU Gen AI from `GenAIkey.md`

---

## File Structure

```
Lab3 set up a local chatbot/
├── README.md              # This file
├── chatbot.html           # Main UI
├── scripts/
│   └── server.py         # Flask backend
├── chatHistory/          # Saved conversations
└── requirements.txt      # Python dependencies
```

---

## API Configuration

- **Kimi API** (if `../Data/Kimi.md` exists): Moonshot AI models
- **HKBU Gen AI** (fallback): Uses `../Data/GenAIkey.md`

Server automatically detects and uses the available API key.

---

**Ready to start? Run `python3 scripts/server.py` and open http://localhost:5000 in your browser!**
