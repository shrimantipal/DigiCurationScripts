import soundfile as sf
import os
import subprocess

def convert_wav_to_mp3(input_file, output_file):
    data, samplerate = sf.read(input_file)
    sf.write(output_file, data, samplerate, format='mp3')
    
# input_file = os.path.abspath("C:/Users/pal10/Desktop/1105039/1105039/preservation/Bill Hall part 2/ZOOM0005.WAV")
# output_file = os.path.abspath("C:/Users/pal10/Desktop/1105039/1105039/preservation/Bill Hall part 2/ZOOM0005.mp3")

# if os.path.exists(input_file):
#     convert_wav_to_mp3(input_file, output_file)
# else:
#     print("Input WAV file does not exist:", input_file)
    

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
        
        if(content!='.ipynb_checkpoints' and content.endswith('.WAV')):
            try: 
                
                input_file = content_path
                output_file_name = f'{content}.mp3'
                output_file = os.path.join(folder_path, output_file_name)
                convert_wav_to_mp3(input_file, output_file)
    
            except Exception as E:
                print(E)
                print("Could not convert!")

def find_subfolder(start_path, find_name):
    # Check if the specified path exists
    if not os.path.exists(start_path):
        print(f"Path {start_path} does not exist.")
        return []

    # Initialize a list to store all folder paths
    req_folders = []
    # Traverse through the directory structure
    for foldername, subfolders, filenames in os.walk(start_path):
        if find_name in subfolders:
            req_folder_path = os.path.join(foldername, find_name)
            req_folders.append(start_path)
            print(f"Found {find_name} folder at: {req_folder_path}")
            convert_files(req_folder_path)

    if not req_folders:
        print(f"No {find_name} folders found in the directory structure.")

    return req_folders

start_path = r'C:\Users\pal10\Desktop\1105039\1105039' # root path variable, has to be changed FIRST.
find = 'OriginalFiles' # the folder that contains the wordstar files. 
find_subfolder(start_path, find)