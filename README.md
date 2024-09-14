# Music Box - Two Octaves Plus A0, B0, and Bb0

## Description

The Music Box is a Python application that simulates a piano with a graphical interface. It covers two octaves plus additional keys A0, B0, and Bb0. Users can interact with the piano by clicking on the keys to play corresponding musical notes. The application uses `tkinter` for the graphical user interface and `pygame` for sound playback.

## Features

- **Two Octaves**: Includes notes from C1 to B2.
- **Extended Range**: Adds A0, B0, and Bb0 for a broader range.
- **Interactive Keys**: Clickable keys to play notes.
- **Sound Playback**: Uses `pygame` to play MP3 files.

## Requirements

- Python 3.x
- `pygame` library
- `tkinter` (included with Python)
- MP3 files for each note (located in the `music/` directory)

## Usage
Run the Application
Execute the Python script:

`python <script-name>.py`
### Interact with the Piano
Click on the piano keys to play the corresponding notes. The name of the currently pressed key will be displayed in the text entry field.

## Code Overview
- pygame Initialization: Configures sound playback.
- tkinter GUI: Creates the visual piano interface.
- Key Mapping: Defines positions and labels for white and black keys.
- Sound Playback: Utilizes pygame.mixer.Sound to handle MP3 playback.

## Example Layout
The piano interface includes:

- White Keys: Natural notes (C, D, E, F, G, A, B) across two octaves.
- Black Keys: Sharp notes (C#, D#, F#, G#, A#) and their flat equivalents.