# M_i-LF — Mechanical Interface-Like Feeling Desktop App ⌨️🔊

> **Get custom mechanical keyboard and vintage typewriter sounds whenever you type anywhere on your laptop!**

**M_i-LF** is an open-source desktop application that hooks into system-wide background keyboard events on macOS, Windows, and Linux. Whenever you type in *any application* (VS Code, Slack, Chrome, Notes, Terminal, etc.), it instantly triggers low-latency acoustic sound profiles from a built-in sound database.

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

## 🚀 Quick Start & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/AnmolM-777/M_i-LF.git
cd M_i-LF
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate Sound Database
Synthesize the baseline 44.1kHz sound packs into the `sounds/` directory:
```bash
python sound_generator.py
```

### 4. Run the App

#### Desktop GUI Mode:
```bash
python main.py
```

#### Headless CLI Mode:
```bash
python main.py --cli --profile typewriter --volume 0.9
```

---

## 🛡️ macOS Accessibility Permission

On macOS, operating systems require Accessibility permission for applications that listen for global background keypresses:
1. Open **System Settings** -> **Privacy & Security** -> **Accessibility**.
2. Enable access for your terminal application (e.g., `Terminal`, `iTerm`, or `VS Code`) or python binary running the app.

---

## 📂 Sound Database Structure (`sounds/`)

You can easily add your own custom sound packs by dropping `.wav` files into `sounds/<your_pack_name>/` and adding a record to `sound_db.json`:

```
sounds/
├── cream_thock/
│   ├── press_regular.wav
│   ├── press_space.wav
│   ├── press_enter.wav
│   ├── press_backspace.wav
│   └── release.wav
├── cherry_mx_blue/
├── typewriter/
├── ibm_model_m/
└── bubble_wrap/
```

---

## 📜 License
MIT License. Open source and free for the custom keyboard enthusiast community!
