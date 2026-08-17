#!/usr/bin/env python3
"""
M_i-LF — Mechanical Interface Like Feeling Desktop Application
Open-Source System-Wide Keyboard Audio Simulator.
"""

import sys
import time
import argparse
from engine import KeyboardAudioEngine, GlobalKeyboardListener
from sound_generator import generate_sound_database
from cli_menu import run_cli_menu

def parse_args():
    parser = argparse.ArgumentParser(description="M_i-LF — Mechanical Interface Keyboard Sound App")
    parser.add_argument("--cli", action="store_true", help="Run in headless CLI background mode without GUI")
    parser.add_argument("--profile", type=str, default="cream_thock", help="Switch sound profile (cream_thock, cherry_mx_blue, typewriter, ibm_model_m, bubble_wrap)")
    parser.add_argument("--volume", type=float, default=0.8, help="Master volume (0.0 to 1.0)")
    parser.add_argument("--synth", action="store_true", help="Re-synthesize the sound database WAV files")
    return parser.parse_args()

def main():
    args = parse_args()

    if args.synth:
        generate_sound_database()

    if args.cli:
        run_cli_menu(profile=args.profile, volume=args.volume)
    else:
        # Attempt launching GUI, fallback to interactive CLI menu if Tkinter is not installed
        try:
            from gui import run_gui
            run_gui()
        except ModuleNotFoundError as e:
            if "_tkinter" in str(e) or "tkinter" in str(e):
                run_cli_menu(profile=args.profile, volume=args.volume)
            else:
                raise e

if __name__ == "__main__":
    main()
