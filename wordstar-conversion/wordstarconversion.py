import sys
import argparse
import os
import shutil
import subprocess
import markdown2
from weasyprint import HTML

def convert_md_to_pdf(input_md_file, output_pdf_file):
    # Read Markdown content from file
    with open(input_md_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown2.markdown(md_content)

    # Create PDF using WeasyPrint
    HTML(string=html_content).write_pdf(output_pdf_file)

def specialchars(x):
    return {
        0x0D : 0,    # skip newline handling
        0x0A : 0,
        0x19 : 0x2A, #italic
        0x13 : 0x2A, #underline->italic
        0x02 : 0x2A, #bold
        0x14 : 0x5E, #superscript
        0x16 : 0x7E, #subscript
        0x18 : 0x7E  #strikethrough
    }.get(x,0)

def handleblock(block):
    # implement here the handling of the blocks
    # block[0] is the length of the block (int)
    # block[2] is the command
    if block[2] == 0x03: # footer
        footerdata = converttext(block[20:]).replace(b'\n',b'')
        return b'^['+footerdata+b']'
    elif block[2] == 0x09: # TAB
        return b'    '
    elif block[2] == 0x11: # paragraph style
        if block[3] == 0x02: # header
            return b'## '
        elif block[3]== 0x05: #title
            return b'# '
    return b''

def converttext(data):
    counter = -1
    newline = False
    linetype = 0
    outdata = bytearray()
    while counter < len(data) - 1:
        counter += 1
        # End of file character
        if data[counter] == 0x1A:
            break
        # Extended character
        elif data[counter] == 0x1B:
            outdata.append(data[counter + 1])
            counter += 2
        # Symmetrical sequence: 1Dh special character
        elif data[counter] == 0x1D:
            jump = int.from_bytes(data[counter + 1:counter + 2], byteorder='little')
            outdata += handleblock(data[counter + 1:counter + jump])
            counter += jump + 2
        elif data[counter] < 0x20:  # special formatting characters
            if data[counter] == 0x0D and not newline:
                outdata += b'\x0D\x0A\x0D\x0A'
                newline = True
                linetype = 0
            # Note: Removed the reference to args.textmode since it's not used here
            c = specialchars(data[counter])
            if not c == 0:
                outdata.append(c)
            if data[counter] == 0x02 or data[counter] == 0x18:
                outdata.append(c)  # duplicating some characters ** and ~~
        elif data[counter] < 0x80:  # other characters
            if newline:
                newline = False
                if data[counter] == 0x2E:  # dotline
                    linetype = 1
            if linetype != 1:  # we are in a dotline => ignore it
                outdata.append(data[counter])
    return outdata

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
          # Set to True if you want unformatted (text) output
        
        if(content!='.ipynb_checkpoints' and content.endswith('.ws')):
            try: 
                
                input_file = content_path
                output_file_name = f'{content}.md'
                output_pdf_name = f'{content}.pdf'
                output_file = os.path.join(folder_path, output_file_name)
                output_file_pdf = os.path.join(folder_path, output_pdf_name)
                text_mode = False  # Set to True if you want unformatted (text) output
                
                # Read file
                print("Reading " + input_file)
                with open(input_file, "rb") as infile:
                    data = infile.read()
                
                # Let's go through the file for some cleanup...
                print("Converting...")
                outdata = converttext(data)
                
                # Now decode the extended ASCII data...
                outstring = outdata.decode("cp437")
                
                # Write to the output file
                with open(output_file, "wt") as outfile:
                    outfile.write(outstring)
                
                print("Conversion ready, " + output_file + " written!")
                convert_md_to_pdf(output_file, output_file_pdf)
    
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

start_path = r'C:\Users\pal10\Desktop\wstest\preservation' # root path variable, has to be changed FIRST.
find = 'OriginalFiles' # the folder that contains the wordstar files. 
find_subfolder(start_path, find)