from tkinter import *
import pygame

# Initialize pygame
pygame.init()

# Set up the main window
root = Tk()
root.title("Music Box - Two Octaves Plus A0, B0, and Bb0")
root.geometry("1700x400+0+0")  # Adjusted for extra keys
root.configure(background="white")

# Create Frames
main_frame = Frame(root, bg="powder blue", bd=10, relief=RIDGE)
main_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

header_frame = Frame(main_frame, bg="powder blue", bd=10, relief=RIDGE)
header_frame.pack(fill=X)

keyboard_frame = Frame(main_frame, bg="powder blue")
keyboard_frame.pack(fill=X, pady=10)

# Function to play sound
def play_sound(note):
    sound = pygame.mixer.Sound(f"music/{note}.mp3")
    sound.play()

# Label
Label(header_frame, text="Piano Musical Keys - Two Octaves Plus A0, B0, and Bb0", font=("Arial", 24, "bold"), padx=8, pady=8, bd=4, width=70, bg="powder blue", fg="white", height=1, justify=CENTER).pack()

# Display Entry
str_var = StringVar()
str_var.set("Piano")
display = Entry(header_frame, textvariable=str_var, font=("Arial", 18, "bold"), width=35, bd=4, bg="powder blue", fg="black", justify=CENTER)
display.pack(pady=5)

# White Keys (natural keys) and Black Keys (sharp keys)
keys = [
    ("A0", -3),("B0", -1), ("C1", 0), ("D1", 1), ("E1", 2), ("F1", 3), ("G1", 4), ("A1", 5), ("B1", 6),
    ("C2", 7), ("D2", 8), ("E2", 9), ("F2", 10), ("G2", 11), ("A2", 12), ("B2", 13)
]

black_keys = [
    ("A#0", -3, "Bb0"), ("C#1", 0, "Db1"), ("D#1", 1, "Eb1"), ("F#1", 3, "Gb1"), ("G#1", 4, "Ab1"), ("A#1", 5, "Bb1"),
    ("C#2", 7, "Db2"), ("D#2", 8, "Eb2"), ("F#2", 10, "Gb2"), ("G#2", 11, "Ab2"), ("A#2", 12, "Bb2")
]

# Create white keys
for key, col in keys:
    Button(keyboard_frame, bd=4, width=6, height=10, text=key, bg="white", fg="black", font=("Arial", 18, "bold"), command=lambda k=key: play_sound(k)).grid(row=0, column=col+4, padx=2, pady=2)

# Create black keys
for key, col, sound_key in black_keys:
    Button(keyboard_frame, bd=4, width=4, height=6, text=key, bg="black", fg="white", font=("Arial", 14, "bold"), command=lambda k=sound_key: play_sound(k)).grid(row=0, column=col+4, padx=(35, 0), pady=2, sticky=N)

# Set up window resizing behavior
root.update_idletasks()
keyboard_frame.update_idletasks()
root.geometry(f'{keyboard_frame.winfo_width()}x{keyboard_frame.winfo_height()}')

# Main loop
root.mainloop()
