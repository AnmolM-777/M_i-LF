"""
Build script to package M_i-LF into a standalone desktop executable / .app bundle.
Uses PyInstaller to bundle sound assets, audio engine, and Tkinter GUI into one executable.
"""

import os
import sys
import subprocess
import shutil

def build_app():
    print("Building standalone M_i-LF desktop application...")

    # Ensure sound assets are generated
    from sound_generator import generate_sound_database
    generate_sound_database()

    # Determine separator for PyInstaller data files (; on Windows, : on Unix)
    sep = ';' if sys.platform == 'win32' else ':'

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name=M_i-LF",
        "--onefile",
        "--windowed",
        f"--add-data=sounds{sep}sounds",
        f"--add-data=sound_db.json{sep}.",
        "main.py"
    ]

    print(f"Running PyInstaller command: {' '.join(cmd)}")
    result = subprocess.run(cmd)

    if result.returncode == 0:
        print("\n========================================================")
        print("🎉 SUCCESS! Standalone desktop app built in dist/ folder:")
        if sys.platform == 'darwin':
            print("   dist/M_i-LF (Executable / macOS App)")
        elif sys.platform == 'win32':
            print("   dist/M_i-LF.exe (Windows Executable)")
        else:
            print("   dist/M_i-LF (Linux Executable)")
        print("========================================================")
    else:
        print("\n❌ Build failed. Please check errors above.")

if __name__ == "__main__":
    build_app()
