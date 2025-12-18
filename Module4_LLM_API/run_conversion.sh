#!/bin/bash

# Script to run the PDF to Markdown conversion

echo "PDF to Markdown Conversion Script"
echo "================================"

# Check if API key is set
if [[ -z "$HKBU_GENAI_API_KEY" ]]; then
    echo "Warning: HKBU_GENAI_API_KEY environment variable not set"
    echo "Please set your API key before running the conversion:"
    echo "export HKBU_GENAI_API_KEY='your-api-key-here'"
    echo ""
    echo "Or create a .env file with your API key"
    exit 1
fi

# Run the conversion script
echo "Starting conversion process..."
python pdf_to_markdown.py

echo "Conversion complete!"