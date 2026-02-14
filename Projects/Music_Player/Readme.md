# Command-Line Music Player (Python)

A simple and lightweight command-line music player built using Python and Pygame. This program allows you to play, pause, resume, and stop audio files directly from the terminal.

## Features
1. Play music from the `Music` directory  
1. Pause currently playing audio  
1. Resume playback  
1. Stop music  
1. Simple command-driven interface  
1. Error handling for missing files  

## Functions
play: Function to play the given music. It uses pygame.mixer.music

## Flow
1. Initializes Pygame.
1. Switches to the Music folder.
1. Listens for user commands.
1. Controls playback using pygame.mixer.music.
1. Handles missing file errors (if any).

## Project Structure
├── Music  
│ └── (place your .mp3/.wav files here)   
├── player.py   
└── README.md

## Dependecies
pygame:
```bash
pip install pygame
```

## Usage
When the program starts, you'll see:
```
Welcome to command-line music player!
Type 'exit' to Exit.
>>
```

#### Available commands:
1. play file_name: Play the specified music file
1. pause: Pause the current music
1. resume: Resume the current music
1. stop: Stop the current music
1. exit: Exit the program

## Conclusion
This is a fun and helpful project for beginners. Please do check it out!
