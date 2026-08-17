"""
Global Low-Latency Audio Engine & OS Key Listener for M_i-LF
Listens for keypresses anywhere across the OS (system-wide background hook)
and plays polyphonic mechanical keyboard sounds from the sound database.
"""

import os
import json
import time
import random
import threading
from pynput import keyboard

# Initialize Pygame Mixer with low latency settings
import pygame

class KeyboardAudioEngine:
    def __init__(self, db_path="sound_db.json", base_dir="."):
        self.base_dir = base_dir
        self.db_path = os.path.join(base_dir, db_path)
        self.is_enabled = True
        self.loaded_sounds = {}
        self.active_keys = set()

        # Low latency audio initialization
        try:
            pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
            pygame.mixer.init()
            pygame.mixer.set_num_channels(32)  # High polyphony for fast typing
        except Exception as e:
            print(f"[Warning] Audio mixer init error: {e}")

        self.load_config()

    def load_config(self):
        if not os.path.exists(self.db_path):
            print(f"[Error] Database file {self.db_path} not found.")
            return

        with open(self.db_path, "r") as f:
            self.config = json.load(f)

        self.active_profile_name = self.config.get("active_profile", "cream_thock")
        self.master_volume = self.config.get("master_volume", 0.8)
        self.pitch_variation = self.config.get("pitch_variation", 0.05)
        self.enable_upstroke = self.config.get("enable_upstroke", True)

        self.load_profile_sounds(self.active_profile_name)

    def load_profile_sounds(self, profile_name):
        profiles = self.config.get("profiles", {})
        if profile_name not in profiles:
            profile_name = "cream_thock"

        profile = profiles[profile_name]
        sound_dir = os.path.join(self.base_dir, profile.get("dir", ""))
        self.active_profile_name = profile_name

        self.loaded_sounds = {}
        for key_type in ["press_regular", "press_space", "press_enter", "press_backspace", "release"]:
            file_name = profile.get(key_type)
            if file_name:
                full_path = os.path.join(sound_dir, file_name)
                if os.path.exists(full_path):
                    try:
                        snd = pygame.mixer.Sound(full_path)
                        snd.set_volume(self.master_volume)
                        self.loaded_sounds[key_type] = snd
                    except Exception as e:
                        print(f"[Error] Failed loading sound {full_path}: {e}")

    def set_profile(self, profile_name):
        self.load_profile_sounds(profile_name)
        self.config["active_profile"] = profile_name
        self.save_config()

    def set_volume(self, volume):
        self.master_volume = max(0.0, min(1.0, volume))
        for snd in self.loaded_sounds.values():
            snd.set_volume(self.master_volume)
        self.config["master_volume"] = self.master_volume
        self.save_config()

    def save_config(self):
        try:
            with open(self.db_path, "w") as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"[Warning] Failed saving config: {e}")

    def play_sound(self, key_type):
        if not self.is_enabled:
            return

        snd = self.loaded_sounds.get(key_type) or self.loaded_sounds.get("press_regular")
        if snd:
            # Play on an available polyphonic channel
            channel = pygame.mixer.find_channel(True)
            if channel:
                channel.play(snd)

class GlobalKeyboardListener:
    """System-wide background keyboard listener using pynput."""

    def __init__(self, audio_engine):
        self.audio_engine = audio_engine
        self.listener = None
        self.is_running = False

    def on_press(self, key):
        key_code = str(key)
        if key_code in self.audio_engine.active_keys:
            return  # Ignore OS auto-repeat key events
        self.audio_engine.active_keys.add(key_code)

        # Categorize key type cleanly
        if key == keyboard.Key.space:
            key_type = "press_space"
        elif key == keyboard.Key.enter:
            key_type = "press_enter"
        elif key == keyboard.Key.backspace:
            key_type = "press_backspace"
        else:
            key_type = "press_regular"

        self.audio_engine.play_sound(key_type)

    def on_release(self, key):
        key_code = str(key)
        self.audio_engine.active_keys.discard(key_code)

        if self.audio_engine.enable_upstroke:
            self.audio_engine.play_sound("release")

    def start(self):
        if self.is_running:
            return
        self.is_running = True
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        print("[M_i-LF Engine] System-wide global keyboard listener ACTIVE.")

    def stop(self):
        if not self.is_running:
            return
        self.is_running = False
        if self.listener:
            self.listener.stop()
        print("[M_i-LF Engine] Keyboard listener stopped.")
