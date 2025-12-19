#!/bin/bash
# Quick start script for Local Chatbot
# Starts the Flask server with proper environment setup

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🤖 Starting Local Chatbot Server..."
echo ""

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate 2>/dev/null || . venv/bin/activate
    echo "✅ Virtual environment activated"
else
    echo "⚠️  Virtual environment not found. Running with system Python."
    echo "   Run ./setup.sh first to create a virtual environment."
fi
echo ""

# Check if dependencies are installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "❌ Flask not found. Installing dependencies..."
    pip install -r requirements.txt
    echo ""
fi

# Check API key
API_KEY_FILE="../Data/GenAIkey.md"
if [ ! -f "$API_KEY_FILE" ]; then
    echo "⚠️  WARNING: API key file not found at: $API_KEY_FILE"
    echo "   The server will start but API calls will fail."
    echo ""
fi

# Start the server
echo "🚀 Starting server on http://localhost:5000"
echo "   Press Ctrl+C to stop"
echo ""
python3 scripts/server.py

