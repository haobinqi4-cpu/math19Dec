#!/bin/bash
# Setup script for Local Chatbot Lab3
# This script helps verify and set up the chatbot environment

echo "=========================================="
echo "🤖 Local Chatbot Setup Script"
echo "=========================================="
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "📁 Working directory: $SCRIPT_DIR"
echo ""

# Step 1: Check Python version
echo "1️⃣ Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "   ✅ Python 3 found: $PYTHON_VERSION"
else
    echo "   ❌ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi
echo ""

# Step 2: Check if virtual environment should be created
echo "2️⃣ Checking for virtual environment..."
if [ ! -d "venv" ]; then
    echo "   📦 Creating virtual environment..."
    python3 -m venv venv
    echo "   ✅ Virtual environment created"
else
    echo "   ✅ Virtual environment already exists"
fi
echo ""

# Step 3: Activate virtual environment and install dependencies
echo "3️⃣ Installing dependencies..."
source venv/bin/activate 2>/dev/null || . venv/bin/activate
pip install --upgrade pip -q
pip install -r requirements.txt
echo "   ✅ Dependencies installed"
echo ""

# Step 4: Check API key
echo "4️⃣ Checking API key..."
API_KEY_FILE="../Data/GenAIkey.md"
if [ -f "$API_KEY_FILE" ]; then
    API_KEY=$(cat "$API_KEY_FILE" | grep -v "^#" | grep -v "^```" | tr -d '\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    if [ ! -z "$API_KEY" ]; then
        echo "   ✅ API key found"
    else
        echo "   ⚠️  API key file exists but appears empty"
    fi
else
    echo "   ⚠️  API key file not found at: $API_KEY_FILE"
    echo "   Please create it with your HKBU Gen AI API key"
fi
echo ""

# Step 5: Create chatHistory directory if it doesn't exist
echo "5️⃣ Setting up directories..."
mkdir -p chatHistory
echo "   ✅ Chat history directory ready"
echo ""

# Step 6: Check if server script exists
echo "6️⃣ Checking server files..."
if [ -f "scripts/server.py" ]; then
    echo "   ✅ Server script found"
else
    echo "   ❌ Server script not found at scripts/server.py"
    exit 1
fi
echo ""

# Step 7: Make scripts executable
chmod +x scripts/server.py 2>/dev/null || true
echo "   ✅ Scripts are executable"
echo ""

echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo ""
echo "To start the chatbot server:"
echo "  1. Activate virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Start the server:"
echo "     python3 scripts/server.py"
echo ""
echo "  3. Open your browser to:"
echo "     http://localhost:5000"
echo ""
echo "Or use the quick start script:"
echo "    ./start.sh"
echo ""

