import os
import sys
import shutil

def move_subfolders_up(folder_path):
    # Check if the specified folder exists
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return
    # Get the list of subfolders in the specified folder
    subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    root_contents = os.listdir(folder_path)
    # Move files up one level
    for content in root_contents:
        content_path = os.path.join(folder_path, content)
        new_path = os.path.join(os.path.dirname(folder_path), content)
        try:
            shutil.move(content_path, new_path)
            print(f"Moved {content} to {new_path}")
        except Exception as E:
            print(f"Error moving {content}: {e}")

    # Move each subfolder up one level
    for subfolder in subfolders:
        subfolder_name = os.path.basename(subfolder)
        new_path = os.path.join(os.path.dirname(folder_path), subfolder_name)
        try:
            shutil.move(subfolder, new_path)
            print(f"Moved {subfolder_name} to {new_path}")
        except Exception as e:
            print(f"Error moving {subfolder_name}: {e}")

    try:
        os.rmdir(folder_path)
        print(f"Deleted {folder_path}")
    except Exception as e:
        print(f"Error deleting {folder_path}: {e}")

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
            move_subfolders_up(req_folder_path)

    if not req_folders:
        print(f"No {find_name} folders found in the directory structure.")

    return req_folders

start_path = r'Z:\IHLC\GreatAmericanPeopleShow - Copy\preservation' 
move_up = '001' # the folder that needs to be deleted. 
find_subfolder(start_path, move_up)