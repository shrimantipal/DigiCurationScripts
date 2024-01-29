import os

def find_subfolder(start_path, dup):
    # Check if the specified path exists
    if not os.path.exists(start_path):
        print(f"Path {start_path} does not exist.")
        return []

    root_contents = os.listdir(dup)

    for content in root_contents:
        content_path = os.path.join(start_path, content)
        # new_path = os.path.join(os.path.dirname(start_path), content)
        print(content_path)
        print(content)
        os.makedirs(content_path, exist_ok=True)
        # subfolder_names = ['OriginalFiles', 'ObjectDocumentation', 'ImageCapturedFromDisk']
        # subfolder_paths = [os.path.join(content_path, subfolder_name) for subfolder_name in subfolder_names]
        # for subfolder_path in subfolder_paths:
        #     os.makedirs(subfolder_path, exist_ok=True)
        #     print(f"Subfolder '{subfolder_path}' created.")


start_path = r'C:\Users\pal10\Desktop\GAPSFiles\GAPSTestsetCopy\access\nearline'
duplicate = r'C:\Users\pal10\Desktop\GAPSFiles\GAPSTestsetCopy\preservation'
find_subfolder(start_path, duplicate)