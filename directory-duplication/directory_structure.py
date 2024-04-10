import os

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


start_path = r'C:\Users\pal10\Desktop\GAPSFiles\GAPSTestsetCopy\access\nearline'
find_subfolder(start_path)