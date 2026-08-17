"""
Interactive CLI Control Panel for M_i-LF
Used when Tkinter GUI is not installed in the system Python environment.
"""

import sys
import time
from engine import KeyboardAudioEngine, GlobalKeyboardListener

def run_cli_menu(profile="cream_thock", volume=0.8):
    print("\n" + "="*60)
    print(" ⌨️  M_i-LF — Mechanical Keyboard Sound Simulator")
    print("==========================================================")
    print(" [Notice] Tkinter GUI not detected. Running Interactive Terminal Mode.")
    print(" System-Wide Audio Listener is ACTIVE across all desktop apps!\n")

    engine = KeyboardAudioEngine()
    engine.set_profile(profile)
    engine.set_volume(volume)

    listener = GlobalKeyboardListener(engine)
    listener.start()

    print_menu(engine)

    try:
        while True:
            cmd = input("\nSelect Option [1-5 for Profile, +/- Volume, M Mute, Q Quit]: ").strip().lower()
            if cmd == '1':
                engine.set_profile('cream_thock')
                print(" -> Active Profile: Creamy Thock (Linear)")
                engine.play_sound("press_space")
            elif cmd == '2':
                engine.set_profile('cherry_mx_blue')
                print(" -> Active Profile: Cherry MX Blue (Clicky)")
                engine.play_sound("press_space")
            elif cmd == '3':
                engine.set_profile('typewriter')
                print(" -> Active Profile: Underwood Typewriter (Vintage)")
                engine.play_sound("press_space")
            elif cmd == '4':
                engine.set_profile('ibm_model_m')
                print(" -> Active Profile: IBM Model M (Buckling Spring)")
                engine.play_sound("press_space")
            elif cmd == '5':
                engine.set_profile('bubble_wrap')
                print(" -> Active Profile: Bubble Wrap (Pop)")
                engine.play_sound("press_space")
            elif cmd == '+' or cmd == '=':
                new_vol = min(1.0, engine.master_volume + 0.1)
                engine.set_volume(new_vol)
                print(f" -> Volume: {int(engine.master_volume * 100)}%")
            elif cmd == '-':
                new_vol = max(0.0, engine.master_volume - 0.1)
                engine.set_volume(new_vol)
                print(f" -> Volume: {int(engine.master_volume * 100)}%")
            elif cmd == 'm':
                engine.is_enabled = not engine.is_enabled
                status = "ACTIVE" if engine.is_enabled else "MUTED"
                print(f" -> Sound Engine: {status}")
            elif cmd == 'q':
                print("\n[M_i-LF] Shutting down sound engine...")
                listener.stop()
                sys.exit(0)
            else:
                print_menu(engine)

    except (KeyboardInterrupt, EOFError):
        print("\n[M_i-LF] Shutting down sound engine...")
        listener.stop()
        sys.exit(0)

def print_menu(engine):
    print("\n--- CONTROLS ---")
    print(f"  Current Profile: {engine.active_profile_name}")
    print(f"  Volume:          {int(engine.master_volume * 100)}%")
    print(f"  Status:          {'ACTIVE' if engine.is_enabled else 'MUTED'}")
    print("\n  Presets:")
    print("    1) Creamy Thock (Linear)")
    print("    2) Cherry MX Blue (Clicky)")
    print("    3) Underwood Typewriter (Vintage)")
    print("    4) IBM Model M (Buckling Spring)")
    print("    5) Bubble Wrap (Pop)")
    print("\n  Commands:")
    print("    [+] Increase Volume   [-] Decrease Volume")
    print("    [m] Toggle Mute       [q] Quit App")
