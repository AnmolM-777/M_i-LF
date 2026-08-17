#!/bin/bash
# 1-Click Launcher Script for macOS & Linux

echo "🚀 Starting M_i-LF Mechanical Keyboard Sound App..."

# Find suitable Python 3 executable (prefer 3.9+)
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

# Check if dependencies are installed, otherwise install with pre-compiled wheels
$PYTHON_CMD -c "import pygame, pynput" 2>/dev/null || $PYTHON_CMD -m pip install --prefer-binary -r requirements.txt

# Run main application
$PYTHON_CMD main.py
