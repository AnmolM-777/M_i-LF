#!/bin/bash
# 1-Click Launcher Script for macOS & Linux (Virtual Environment Auto-Setup)

echo "🚀 Starting M_i-LF Mechanical Keyboard Sound App..."

# Find Python 3 executable
PYTHON_CMD=""
for cmd in python3.12 python3.11 python3.10 python3.9 python3; do
    if command -v $cmd &> /dev/null; then
        PYTHON_CMD=$cmd
        break
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    echo "❌ Python 3 is required. Please install Python 3."
    exit 1
fi

echo "Using Python: $($PYTHON_CMD --version)"

# Create a local isolated virtual environment (.venv) if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating isolated Python environment (.venv)..."
    $PYTHON_CMD -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install / update dependencies cleanly inside .venv
echo "⚙️  Verifying dependencies..."
pip install --prefer-binary -r requirements.txt > /dev/null 2>&1

# Run main application using virtual environment python
echo "⌨️  Launching M_i-LF Sound Engine..."
python main.py
