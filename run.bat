@echo off
title M_i-LF — Mechanical Keyboard Sound App
echo Starting M_i-LF Mechanical Keyboard Sound App...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3 is required. Please install Python.
    pause
    exit /b
)

python -c "import pygame, pynput" >nul 2>&1
if %errorlevel% neq 0 (
    pip install -r requirements.txt
)

python main.py
