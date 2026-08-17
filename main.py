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
        print("==========================================================")
        print(" ⌨️  M_i-LF CLI Mode — Global Keyboard Sound Engine")
        print("==========================================================")
        engine = KeyboardAudioEngine()
        engine.set_profile(args.profile)
        engine.set_volume(args.volume)

        listener = GlobalKeyboardListener(engine)
        listener.start()

        print(f"[M_i-LF] Active Profile: {args.profile}")
        print(f"[M_i-LF] Volume: {int(args.volume * 100)}%")
        print("[M_i-LF] Press Ctrl+C in terminal to stop.")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[M_i-LF] Shutting down...")
            listener.stop()
            sys.exit(0)
    else:
        # Run GUI Mode
        from gui import run_gui
        run_gui()

if __name__ == "__main__":
    main()
