#!/bin/bash
# 1-Click Launcher Script for macOS & Linux

echo "🚀 Starting M_i-LF Mechanical Keyboard Sound App..."

# Check Python environment
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required. Please install Python 3."
    exit 1
fi

# Install dependencies if missing
python3 -c "import pygame, pynput" 2>/dev/null || pip3 install -r requirements.txt

# Run main application
python3 main.py
