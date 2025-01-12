import tkinter as tk
from pygame import mixer
import random

# Initialize the sound mixer
mixer.init()

# Function to play a specific note
def play_note(note):
    mixer.music.load(f"sounds/{note}.mp3")
    mixer.music.play()

# Function to handle key presses
def on_key_press(event):
    key_map = {
        'a': 'C',
        's': 'D',
        'd': 'E',
        'f': 'F',
        'g': 'G',
        'h': 'A',
        'j': 'B',
        'w': 'C#',
        'e': 'D#',
        't': 'F#',
        'y': 'G#',
        'u': 'A#'
    }
    note = key_map.get(event.char.lower())
    if note:
        play_note(note)
        highlight_key(note)

# Function to simulate random key presses with random timing
def random_key_press():
    key_list = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'w', 'e', 't', 'y', 'u']
    random_key = random.choice(key_list)
    event = tk.Event()
    event.char = random_key
    on_key_press(event)
    random_delay = random.randint(500, 1500)  # Random delay between 500ms and 1500ms
    root.after(random_delay, random_key_press)  # Call this function again after a random delay

# Function to highlight the key when pressed
def highlight_key(note):
    key_colors = {
        'C': (0, "white"), 'D': (1, "white"), 'E': (2, "white"), 'F': (3, "white"), 'G': (4, "white"), 'A': (5, "white"), 'B': (6, "white"),
        'C#': (0.75, "black"), 'D#': (1.75, "black"), 'F#': (3.75, "black"), 'G#': (4.75, "black"), 'A#': (5.75, "black")
    }
    if note in key_colors:
        position, color = key_colors[note]
        if color == "white":
            x1, y1, x2, y2 = position * 100, 0, (position + 1) * 100, 200
        else:
            x1, y1, x2, y2 = position * 100 + 0, 0, position * 100 + 50, 120
        rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill="grey", outline="black")
        root.after(200, lambda: canvas.delete(rect_id))

# Create the main application window
root = tk.Tk()
root.title("Piano Keyboard")
root.geometry("800x300")

# Create a canvas for the piano layout
canvas = tk.Canvas(root, width=700, height=280)
canvas.pack()

# Draw white keys
white_keys = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
white_key_width = 100
for i, key in enumerate(white_keys):
    canvas.create_rectangle(i * white_key_width, 0, (i + 1) * white_key_width, 200, fill="white", outline="black")
    canvas.create_text((i * white_key_width) + 50, 150, text=key, font=("Arial", 16))

# Draw black keys
black_keys = {'C#': 75, 'D#': 175, 'F#': 375, 'G#': 475, 'A#': 575}
for key, x_offset in black_keys.items():
    canvas.create_rectangle(x_offset, 0, x_offset + 50, 120, fill="black", outline="black")
    canvas.create_text(x_offset + 25, 90, text=key, fill="white", font=("Arial", 12))

# Bind keypress events
root.bind("<KeyPress>", on_key_press)

# Start simulating random key presses
random_key_press()

# Start the Tkinter event loop
root.mainloop()
