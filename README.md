## Backstory
One of my friends was writing notes for her psychology lectures and had been telling me that her lecturer spoke so fast that she was rewinding every minute or so to make sure her notes were correct.  As a friend, I thought I'd help her out by making a program to transcribe all the audio :) 

### TLDR: 
Friend writing notes for lectures, I made a program to transcribe it all for her.

Mostly [OpenAI's Whisper](https://openai.com/blog/whisper/) did the heavy lifting;  I wrote the accompanying code to make the audio file into a text file. 

## Installation Instructions

### 1. Install FFmpeg
Whisper also requires [FFmpeg](https://ffmpeg.org/), an audio-processing library. If FFmpeg is not already installed on your machine, use one of the below commands to install it.

For Mac users:

    brew install ffmpeg
For Windows users:

    chco install ffmpeg
    
For Linux users:

    Linux sudo apt update && sudo apt install ffmpeg

### 2. Install Whisper and pydub
In the terminal: 

       pip install git+https://github.com/openai/whisper.git
       pip install pydub

### 3. Add your file to the same folder as transcribe.py


### 4. Run the program

In the terminal: 

    python transcribe.py

## What did I learn?
- Revised Python f-strings
- Revised opening a file 
- Creating and writing a text file in Python

## Next time
- Make a user-friendly GUI for the program

