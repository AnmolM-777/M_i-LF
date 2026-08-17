"""
M_i-LF Desktop GUI Application Control Panel
Built with Python Tkinter for cross-platform modern interface.
"""

import sys
import tkinter as tk
from tkinter import ttk, messagebox
from engine import KeyboardAudioEngine, GlobalKeyboardListener

class KeyboardSoundAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("M_i-LF — Mechanical Keyboard Sound Engine")
        self.root.geometry("460x520")
        self.root.resizable(False, False)

        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Custom Colors
        self.bg_color = "#12141d"
        self.card_bg = "#1b1e2b"
        self.accent_color = "#00f2fe"
        self.text_color = "#f0f3f8"
        self.text_muted = "#8a94a6"

        self.root.configure(bg=self.bg_color)

        # Initialize Core Engine & Listener
        self.engine = KeyboardAudioEngine()
        self.listener = GlobalKeyboardListener(self.engine)
        self.listener.start()

        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        # Header Container
        header_frame = tk.Frame(self.root, bg=self.bg_color, pady=16)
        header_frame.pack(fill="x", px=20)

        title_lbl = tk.Label(
            header_frame, 
            text="⌨️ M_i-LF Pro", 
            font=("Helvetica", 18, "bold"), 
            bg=self.bg_color, 
            fg=self.accent_color
        )
        title_lbl.pack(anchor="w")

        subtitle_lbl = tk.Label(
            header_frame, 
            text="Mechanical Interface Sound Simulator • Global OS Listener", 
            font=("Helvetica", 9), 
            bg=self.bg_color, 
            fg=self.text_muted
        )
        subtitle_lbl.pack(anchor="w")

        # Global Active Toggle Card
        toggle_card = tk.Frame(self.root, bg=self.card_bg, bd=1, relief="solid", highlightthickness=0)
        toggle_card.pack(fill="x", padx=20, pady=8, ipady=8)

        self.status_var = tk.StringVar(value="ACTIVE")
        self.is_active_var = tk.BooleanVar(value=True)

        status_lbl = tk.Label(
            toggle_card, 
            text="System-Wide Sound Engine:", 
            font=("Helvetica", 10, "bold"), 
            bg=self.card_bg, 
            fg=self.text_color
        )
        status_lbl.pack(side="left", padx=15)

        self.toggle_btn = tk.Button(
            toggle_card, 
            text="ON", 
            font=("Helvetica", 10, "bold"), 
            bg="#10ac84", 
            fg="#ffffff", 
            activebackground="#0e9b76",
            width=8,
            command=self.toggle_engine
        )
        self.toggle_btn.pack(side="right", padx=15)

        # Profile Switcher Card
        profile_card = tk.LabelFrame(
            self.root, 
            text=" Sound Profiles ", 
            font=("Helvetica", 10, "bold"),
            bg=self.card_bg, 
            fg=self.accent_color,
            padx=15, 
            pady=15
        )
        profile_card.pack(fill="x", padx=20, pady=10)

        self.profile_var = tk.StringVar(value=self.engine.active_profile_name)

        profiles = [
            ("Creamy Thock (Linear)", "cream_thock"),
            ("Cherry MX Blue (Clicky)", "cherry_mx_blue"),
            ("Underwood Typewriter (Vintage)", "typewriter"),
            ("IBM Model M (Buckling Spring)", "ibm_model_m"),
            ("Bubble Wrap (Pop)", "bubble_wrap")
        ]

        for text, key in profiles:
            rb = tk.Radiobutton(
                profile_card,
                text=text,
                value=key,
                variable=self.profile_var,
                font=("Helvetica", 10),
                bg=self.card_bg,
                fg=self.text_color,
                selectcolor="#262b3d",
                activebackground=self.card_bg,
                activeforeground=self.accent_color,
                command=self.on_profile_change
            )
            rb.pack(anchor="w", pady=3)

        # Acoustic Settings Card
        settings_card = tk.LabelFrame(
            self.root, 
            text=" Acoustic Tuning ", 
            font=("Helvetica", 10, "bold"),
            bg=self.card_bg, 
            fg=self.accent_color,
            padx=15, 
            pady=15
        )
        settings_card.pack(fill="x", padx=20, pady=10)

        vol_lbl = tk.Label(settings_card, text="Master Volume:", font=("Helvetica", 9, "bold"), bg=self.card_bg, fg=self.text_color)
        vol_lbl.pack(anchor="w")

        self.vol_scale = tk.Scale(
            settings_card, 
            from_=0, 
            to=100, 
            orient="horizontal", 
            bg=self.card_bg, 
            fg=self.accent_color,
            highlightthickness=0,
            troughcolor="#12141d",
            command=self.on_volume_change
        )
        self.vol_scale.set(int(self.engine.master_volume * 100))
        self.vol_scale.pack(fill="x", pady=4)

        # Upstroke Toggle
        self.upstroke_var = tk.BooleanVar(value=self.engine.enable_upstroke)
        upstroke_cb = tk.Checkbutton(
            settings_card,
            text="Play key release (upstroke) acoustic rebound",
            variable=self.upstroke_var,
            font=("Helvetica", 9),
            bg=self.card_bg,
            fg=self.text_color,
            selectcolor="#262b3d",
            activebackground=self.card_bg,
            command=self.on_upstroke_toggle
        )
        upstroke_cb.pack(anchor="w", pady=6)

        # Footer Info
        footer_lbl = tk.Label(
            self.root, 
            text="Type anywhere on your laptop (Browser, VS Code, Notes, Slack) to hear sounds!", 
            font=("Helvetica", 8, "italic"), 
            bg=self.bg_color, 
            fg=self.text_muted
        )
        footer_lbl.pack(pady=10)

    def toggle_engine(self):
        is_on = not self.engine.is_enabled
        self.engine.is_enabled = is_on
        if is_on:
            self.toggle_btn.configure(text="ON", bg="#10ac84")
        else:
            self.toggle_btn.configure(text="MUTED", bg="#e74c3c")

    def on_profile_change(self):
        selected = self.profile_var.get()
        self.engine.set_profile(selected)
        # Test sample thock sound
        self.engine.play_sound("press_space")

    def on_volume_change(self, val):
        volume = float(val) / 100.0
        self.engine.set_volume(volume)

    def on_upstroke_toggle(self):
        self.engine.enable_upstroke = self.upstroke_var.get()

    def on_close(self):
        self.listener.stop()
        self.root.destroy()

def run_gui():
    root = tk.Tk()
    app = KeyboardSoundAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
