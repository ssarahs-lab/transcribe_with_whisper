## :book: Backstory  
*One of my friends was writing notes for her psychology lectures and had been telling me that her lecturer spoke so fast that she was rewinding every minute or so to make sure her notes were correct.  As a friend, I thought I'd help her out by making a program to transcribe all the audio :)* 

###  :fast_forward:  TLDR
Friend writing notes for lectures, I made a program to transcribe it all for her.

Mostly [OpenAI's Whisper](https://openai.com/blog/whisper/) did the heavy lifting;  I wrote the accompanying code to make the audio file into a text file. 

## :electric_plug: Installation Instructions 

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Install FFmpeg


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![commands for Linux/MacOS/Windows](https://i.imgur.com/AETpOdt.png)

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Install Whisper and pydub
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In the terminal: 

       pip install git+https://github.com/openai/whisper.git
       pip i

### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Add your file to the same folder as transcribe.py


### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4. Run the program

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In the terminal: 

    python transcribe.py

## :raising_hand: What did I learn? 
- Revised Python f-strings
- Revised opening a file 
- Creating and writing a text file in Python

## :information_desk_person: Next time 
- Make a user-friendly GUI for the program
- Make some open source edits to Whisper, my friend made a few edits to her notes so will move onto comparing the original text with the edited text. :open_mouth:
