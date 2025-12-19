# 🚀 Quick Start Guide - Local Chatbot

## Fast Setup (3 Steps)

### Option 1: Automated Setup (Recommended)

```bash
cd "/Users/simonwang/Documents/Usage/MathAI/math19Dec/Lab3 set up a local chatbot"
./setup.sh
./start.sh
```

Then open: **http://localhost:5000**

---

### Option 2: Manual Setup

#### Step 1: Install Dependencies

```bash
cd "/Users/simonwang/Documents/Usage/MathAI/math19Dec/Lab3 set up a local chatbot"
pip install -r requirements.txt
```

#### Step 2: Verify API Key

Make sure your API key exists at:
```
../Data/GenAIkey.md
```

#### Step 3: Start Server

```bash
python3 scripts/server.py
```

#### Step 4: Open Browser

Navigate to: **http://localhost:5000**

---

## What You'll See

### Sidebar (Left)
- **Model Selection**: Choose from 14+ LLMs
- **System Prompt**: Define AI behavior
- **File Context**: Add files for context
- **Chat History**: Save/load conversations

### Chat Area (Right)
- **Message History**: Conversation display
- **Input Box**: Type your messages
- **Send Button**: Submit messages

---

## First Steps

1. **Select a Model**: Choose GPT-5, Gemini 2.5, or others
2. **Set System Prompt** (optional): Define AI's role
3. **Type a Message**: Start chatting!
4. **Add Files** (optional): Provide context files

---

## Example System Prompts

### Data Analyst
```
You are a data analysis expert. Provide clear Python code, 
statistical insights, and visualizations.
```

### Code Reviewer
```
You are a senior software engineer. Review code for best 
practices, performance, and security.
```

### Math Tutor
```
You are a mathematics tutor for MSc students. Explain 
concepts clearly with examples and proofs.
```

---

## Troubleshooting

### Server won't start?
```bash
# Check if port 5000 is in use
lsof -i :5000

# Use a different port: Edit scripts/server.py
# Change: port=5000  to  port=8080
```

### API key error?
```bash
# Check if file exists
ls -la ../Data/GenAIkey.md

# Verify content (don't share!)
cat ../Data/GenAIkey.md
```

### Dependencies missing?
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Features

✨ **Multi-Model**: 14+ LLMs available  
📝 **Custom Prompts**: Define AI behavior  
📎 **File Context**: Upload multiple files  
💾 **Save/Load**: Chat history management  
🎨 **Modern UI**: Beautiful, responsive design  

---

## Next Steps

- Read full [README.md](README.md) for detailed documentation
- Check [setupChatbot.md](setupChatbot.md) for development notes
- Explore different models and their capabilities
- Try adding files for context-aware conversations

---

**Happy Chatting! 🤖**

