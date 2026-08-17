"""
Sound Database Synthesizer & Generator for M_i-LF
Generates high-quality 44.1kHz 16-bit PCM WAV audio files for mechanical switches,
typewriters, and custom acoustic sound profiles into the sounds/ database folder.
"""

import os
import wave
import math
import struct
import random

SAMPLE_RATE = 44100

def create_wav_file(filepath, num_samples, generator_func):
    """Utility to generate and write a 16-bit mono WAV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with wave.open(filepath, 'w') as wav_file:
        wav_file.setnchannels(1)       # Mono
        wav_file.setsampwidth(2)       # 16-bit
        wav_file.setframerate(SAMPLE_RATE)
        
        frames = []
        for i in range(num_samples):
            t = i / SAMPLE_RATE
            val = generator_func(t, i, num_samples)
            # Clamp to -1.0 to 1.0
            val = max(-1.0, min(1.0, val))
            sample = int(val * 32767)
            frames.append(struct.pack('<h', sample))
            
        wav_file.writeframes(b''.join(frames))

def generate_sound_database(base_dir="sounds"):
    """Populates the sound database with various keyboard sound profiles."""
    print("Synthesizing sound database WAV files...")

    # --------------------------------------------------------------------------
    # 1. Creamy Thock Profile (Deep lubricated linear switches)
    # --------------------------------------------------------------------------
    def cream_thock_gen(freq, decay, noise_amt):
        def sample_fn(t, i, total):
            env = math.exp(-t * decay)
            sub = math.sin(2 * math.pi * freq * t * (1 - 0.5 * (i/total)))
            noise = (random.random() * 2 - 1) * math.exp(-t * 200) * noise_amt
            return (sub * 0.7 + noise * 0.3) * env
        return sample_fn

    dir_cream = os.path.join(base_dir, "cream_thock")
    create_wav_file(os.path.join(dir_cream, "press_regular.wav"), int(SAMPLE_RATE * 0.06), cream_thock_gen(110, 45, 0.4))
    create_wav_file(os.path.join(dir_cream, "press_space.wav"), int(SAMPLE_RATE * 0.08), cream_thock_gen(75, 35, 0.5))
    create_wav_file(os.path.join(dir_cream, "press_enter.wav"), int(SAMPLE_RATE * 0.07), cream_thock_gen(90, 40, 0.45))
    create_wav_file(os.path.join(dir_cream, "press_backspace.wav"), int(SAMPLE_RATE * 0.065), cream_thock_gen(95, 42, 0.4))
    create_wav_file(os.path.join(dir_cream, "release.wav"), int(SAMPLE_RATE * 0.03), cream_thock_gen(350, 120, 0.2))

    # --------------------------------------------------------------------------
    # 2. Cherry MX Blue Profile (Clicky tactile snap)
    # --------------------------------------------------------------------------
    def cherry_blue_gen(click_freq, decay):
        def sample_fn(t, i, total):
            env = math.exp(-t * decay)
            # High click + lower bottom out
            click = math.sin(2 * math.pi * click_freq * t * math.exp(-t * 100))
            thock = math.sin(2 * math.pi * 180 * t) * math.exp(-t * 50)
            return (click * 0.6 + thock * 0.4) * env
        return sample_fn

    dir_blue = os.path.join(base_dir, "cherry_mx_blue")
    create_wav_file(os.path.join(dir_blue, "press_regular.wav"), int(SAMPLE_RATE * 0.04), cherry_blue_gen(2200, 70))
    create_wav_file(os.path.join(dir_blue, "press_space.wav"), int(SAMPLE_RATE * 0.06), cherry_blue_gen(1800, 50))
    create_wav_file(os.path.join(dir_blue, "press_enter.wav"), int(SAMPLE_RATE * 0.05), cherry_blue_gen(2000, 60))
    create_wav_file(os.path.join(dir_blue, "press_backspace.wav"), int(SAMPLE_RATE * 0.045), cherry_blue_gen(2100, 65))
    create_wav_file(os.path.join(dir_blue, "release.wav"), int(SAMPLE_RATE * 0.025), cherry_blue_gen(2800, 140))

    # --------------------------------------------------------------------------
    # 3. Vintage Typewriter Profile (Iron strike + bell on enter)
    # --------------------------------------------------------------------------
    def typewriter_strike(t, i, total):
        env = math.exp(-t * 40)
        strike = math.sin(2 * math.pi * 480 * t * math.exp(-t * 20))
        metal_noise = (random.random() * 2 - 1) * math.exp(-t * 90) * 0.5
        return (strike * 0.6 + metal_noise * 0.4) * env

    def typewriter_bell(t, i, total):
        env = math.exp(-t * 4)  # Long bell ring
        bell = math.sin(2 * math.pi * 2650 * t) + 0.3 * math.sin(2 * math.pi * 5300 * t)
        return bell * env * 0.5

    dir_tw = os.path.join(base_dir, "typewriter")
    create_wav_file(os.path.join(dir_tw, "press_regular.wav"), int(SAMPLE_RATE * 0.06), typewriter_strike)
    create_wav_file(os.path.join(dir_tw, "press_space.wav"), int(SAMPLE_RATE * 0.08), lambda t, i, total: typewriter_strike(t, i, total) * 1.2)
    create_wav_file(os.path.join(dir_tw, "press_enter.wav"), int(SAMPLE_RATE * 0.7), typewriter_bell)
    create_wav_file(os.path.join(dir_tw, "press_backspace.wav"), int(SAMPLE_RATE * 0.05), typewriter_strike)
    create_wav_file(os.path.join(dir_tw, "release.wav"), int(SAMPLE_RATE * 0.03), lambda t, i, total: math.sin(2 * math.pi * 800 * t) * math.exp(-t * 100) * 0.2)

    # --------------------------------------------------------------------------
    # 4. IBM Model M Profile (Buckling spring ping)
    # --------------------------------------------------------------------------
    def ibm_buckling(t, i, total):
        env = math.exp(-t * 50)
        ping = math.sin(2 * math.pi * 1750 * t) * 0.4
        chassis = math.sin(2 * math.pi * 140 * t) * 0.6
        return (ping + chassis) * env

    dir_ibm = os.path.join(base_dir, "ibm_model_m")
    create_wav_file(os.path.join(dir_ibm, "press_regular.wav"), int(SAMPLE_RATE * 0.07), ibm_buckling)
    create_wav_file(os.path.join(dir_ibm, "press_space.wav"), int(SAMPLE_RATE * 0.09), lambda t, i, total: ibm_buckling(t, i, total) * 1.3)
    create_wav_file(os.path.join(dir_ibm, "press_enter.wav"), int(SAMPLE_RATE * 0.08), ibm_buckling)
    create_wav_file(os.path.join(dir_ibm, "press_backspace.wav"), int(SAMPLE_RATE * 0.07), ibm_buckling)
    create_wav_file(os.path.join(dir_ibm, "release.wav"), int(SAMPLE_RATE * 0.035), lambda t, i, total: math.sin(2 * math.pi * 1500 * t) * math.exp(-t * 110) * 0.2)

    # --------------------------------------------------------------------------
    # 5. Bubble Wrap Pop Profile
    # --------------------------------------------------------------------------
    def bubble_pop(t, i, total):
        env = math.exp(-t * 120)
        pop = math.sin(2 * math.pi * (500 + t * 4000) * t)
        return pop * env

    dir_pop = os.path.join(base_dir, "bubble_wrap")
    create_wav_file(os.path.join(dir_pop, "press_regular.wav"), int(SAMPLE_RATE * 0.035), bubble_pop)
    create_wav_file(os.path.join(dir_pop, "press_space.wav"), int(SAMPLE_RATE * 0.04), bubble_pop)
    create_wav_file(os.path.join(dir_pop, "press_enter.wav"), int(SAMPLE_RATE * 0.04), bubble_pop)
    create_wav_file(os.path.join(dir_pop, "press_backspace.wav"), int(SAMPLE_RATE * 0.035), bubble_pop)
    create_wav_file(os.path.join(dir_pop, "release.wav"), int(SAMPLE_RATE * 0.02), lambda t, i, total: 0)

    print("Sound database generation completed successfully!")

if __name__ == "__main__":
    generate_sound_database()
