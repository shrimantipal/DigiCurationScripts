import soundfile as sf
import os
import subprocess

def convert_wav_to_mp3(input_file, output_file):
    data, samplerate = sf.read(input_file)
    sf.write(output_file, data, samplerate, format='mp3')
    
input_file = os.path.abspath("C:/Users/pal10/Desktop/1105039/1105039/preservation/Bill Hall part 2/ZOOM0005.WAV")
output_file = os.path.abspath("C:/Users/pal10/Desktop/1105039/1105039/preservation/Bill Hall part 2/ZOOM0005.mp3")

if os.path.exists(input_file):
    convert_wav_to_mp3(input_file, output_file)
else:
    print("Input WAV file does not exist:", input_file)