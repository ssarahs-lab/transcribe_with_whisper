
from os import path; 
from pydub import AudioSegment
import whisper


input = input("Type in the file name without the extension: \n")

                                                    
sound = AudioSegment.from_mp3(f"{input}.mp3")
sound.export("transcript.wav", format="wav")
print("Audio converted")

model = whisper.load_model("base")
result = model.transcribe("transcript.wav")
print("Transcribing..")

lines = result["text"]

with open(f'{input}.txt', 'w') as f:
    f.write(lines)

print(f"All done! The transcription is inside {input}.txt \n Rename the file to something you like and enjoy!")

