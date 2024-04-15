import soundfile as sf
import os
import subprocess
from scipy.signal import resample_poly


def convert_wav_to_mp3(input_file, output_file, target_sr=44100):
    data, samplerate = sf.read(input_file)
    # Resample the audio data if the sample rate is not supported
    if samplerate != target_sr:
        num = target_sr
        den = samplerate
        data = resample_poly(data, num, den)
        samplerate = target_sr
        
    sf.write(output_file, data, samplerate, format='mp3')
    
def transform_file_path(file_path):

    components = file_path.split(os.sep)
    
    preservation_index = components.index('preservation')
    
    components[preservation_index] = r"access/nearline"
    access = r"access/nearline"
    
    new_file_path = os.sep.join(components[:-1])  # Remove the last directory
    #new_file_path = os.path.join(new_file_path, access)
    print(new_file_path)
    return new_file_path

def find_subfolder(dup):

    if not os.path.exists(start_path):
        print(f"Path {start_path} does not exist.")
        return []

    contents = os.listdir(dup)

    for content in contents:
        
        content_path = os.path.join(dup, content)
        
        if os.path.isdir(content_path):
            print(f"Entering subfolder: {content_path}")
            create = content_path.replace("preservation", "access/nearline")
            os.makedirs(create, exist_ok=True)
            find_subfolder(content_path)

        else:
            print(os.path.dirname(content_path))


def convert_files(folder_path):
    # Check if the specified folder exists
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return
    # Get the list of subfolders in the specified folder
    # subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    root_contents = os.listdir(folder_path)
    i = 0
    for content in root_contents:
        content_path = os.path.join(folder_path, content)
        print(content_path)        
        i = i+1
        
        if(content.endswith('.WAV') or content.endswith('.wav')):
            try: 
                
                input_file = content_path
                name = content.replace('.wav', '')
                name = name.replace('.WAV', '')
                output_file_name = f'{name}.mp3'
                access_path = transform_file_path(folder_path)
                print(access_path)
                output_file = os.path.join(access_path, output_file_name)
                print(output_file)
                convert_wav_to_mp3(input_file, output_file)
    
            except Exception as E:
                print(E)
                print("Could not convert!")
                
start_path = r'C:\Users\pal10\Downloads\2620157\2620157\preservation' # root path variable, has to be changed FIRST.
find_subfolder(start_path)
convert_files(start_path)