import subprocess
import os

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

def convert_to_jpg(input_file, output_file):
    command = [
        "/Applications/GraphicConverter 12.app/Contents/MacOS/GraphicConverter 12",
        "-convert",
        f"{input_file}",
        "-to",
        f"{output_file}"
    ]
    
    # Execute the command
    try:
        subprocess.run(command, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}.")

def convert_files(folder_path):

    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return
    
    contents = os.listdir(folder_path)
    
    for content in contents:
        
        content_path = os.path.join(folder_path, content)
        
        if os.path.isdir(content_path):
            print(f"Entering subfolder: {content_path}")
            convert_files(content_path)
        else:
            print("Found file:", content_path)
            if(content.endswith('.pic') or content.endswith('.PIC')):
                try: 
                        
                    input_file = content_path
                    name = content.replace('.pic', '')
                    name = name.replace('.PIC', '')
                    output_file_name = f'{name}.jpg'
                    access_path = transform_file_path(folder_path)
                    print(access_path)
                    output_file = os.path.join(access_path, output_file_name)
                    print(output_file)
                    convert_to_jpg(input_file, output_file)
            
                except Exception as E:
                    print(E)
                    print("Could not convert!") 

start_path = r"/Users/pal10/Desktop/testcollection/preservation" 
find_subfolder(start_path)
convert_files(start_path)