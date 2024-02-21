import soundfile as sf
import os
import subprocess

def convert_wav_to_mp3(input_file, output_file):
    data, samplerate = sf.read(input_file)
    sf.write(output_file, data, samplerate, format='mp3')
    print("Converted!")
    
def transform_file_path(file_path):
    # Split the file path into components
    components = file_path.split(os.sep)
    
    # Find the index of 'preservation'
    preservation_index = components.index('preservation')
    
    # Replace 'preservation' with 'access\nearline'
    components[preservation_index] = r"access\nearline"
    access = r"access\nearline"
    
    # Join the components back into a file path
    new_file_path = os.sep.join(components[:-1])  # Remove the last directory
    new_file_path = os.path.join(new_file_path, access)
    print(new_file_path)
    return new_file_path

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
convert_files(start_path)