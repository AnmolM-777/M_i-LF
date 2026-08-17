# M_i-LF — Mechanical Interface-Like Feeling Desktop App ⌨️🔊

> **Get custom mechanical keyboard and vintage typewriter sounds whenever you type anywhere on your laptop!**

**M_i-LF** is an open-source desktop application that hooks into system-wide background keyboard events on macOS, Windows, and Linux. Whenever you type in *any application* (VS Code, Slack, Chrome, Notes, Terminal, etc.), it instantly triggers low-latency acoustic sound profiles from a built-in sound database.

---

## 💾 How to Run & Download

### Option 1: One-Click Instant Launch (Easiest)

1. Clone or download this repository.
2. Double click **`run.sh`** (on macOS / Linux) or **`run.bat`** (on Windows).
3. The desktop GUI app will launch automatically!

```bash
# On macOS / Linux:
chmod +x run.sh
./run.sh

# On Windows:
run.bat
```

---

### Option 2: Download Standalone Executable App (.app / .exe)

You can download pre-compiled standalone executables directly from the **[GitHub Releases](https://github.com/AnmolM-777/M_i-LF/releases)** page:

| Operating System | Download File | Notes |
| :--- | :--- | :--- |
| 🍏 **macOS** | [`M_i-LF-macOS.zip`](https://github.com/AnmolM-777/M_i-LF/releases) | Double click `M_i-LF` to open |
| 🪟 **Windows** | [`M_i-LF-Windows.zip`](https://github.com/AnmolM-777/M_i-LF/releases) | Contains `M_i-LF.exe` standalone |
| 🐧 **Linux** | [`M_i-LF-Linux.tar.gz`](https://github.com/AnmolM-777/M_i-LF/releases) | Standalone binary |

---

### Option 3: Build Standalone Desktop Executable Yourself

Want to package the app into a standalone binary yourself? Run:

```bash
pip install -r requirements.txt
pip install pyinstaller
python build.py
```
The compiled application will be generated in `dist/M_i-LF`.

---

## ✨ Features

- **System-Wide Background Listening**: Works globally across all desktop apps without needing to keep focus on the app window.
- **Ultra-Low Latency Sound Engine**: Uses polyphonic `pygame.mixer` with small buffer sizes (`512`) for instantaneous sound output while typing fast.
- **Extensible Sound Database (`sounds/` & `sound_db.json`)**:
  - **Creamy Thock**: Deep lubricated linear switch acoustics.
  - **Cherry MX Blue**: Crisp clicky tactile snap.
  - **Underwood Typewriter**: 1920s iron key strikes with return bell on `Enter`.
  - **IBM Model M**: Heavy metallic buckling spring & chassis ping.
  - **Bubble Wrap**: Satisfying air pop sounds.
- **Cross-Platform**: Runs natively on macOS, Windows, and Linux.
- **Desktop GUI & Headless CLI Modes**: Full Tkinter desktop GUI control panel + background CLI launcher.

---

## 🛡️ macOS Accessibility Permission

On macOS, operating systems require Accessibility permission for applications that listen for global background keypresses:
1. Open **System Settings** -> **Privacy & Security** -> **Accessibility**.
2. Enable access for your terminal application (e.g., `Terminal`, `iTerm`, or `VS Code`) or the `M_i-LF` app binary.

---

## 📜 License
MIT License. Open source and free for the custom keyboard enthusiast community!
