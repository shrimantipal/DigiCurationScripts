import subprocess
import os
import sys
import shutil
import argparse
import markdown2
from weasyprint import HTML
import stat
import time
import pandas as pd
from scipy.signal import resample_poly
import soundfile as sf

current_dir = os.getcwd()
unoconv_path = os.path.join(current_dir, "Scripts", "unoconv")
print(unoconv_path)

def transform_file_path(file_path):

    components = file_path.split(os.sep)
    
    preservation_index = components.index('preservation')
    
    components[preservation_index] = r"access\nearline"
    access = r"access\nearline"
    new_file_path = os.sep.join(components[:-1])  # Remove the last directory
    #new_file_path = os.path.join(new_file_path, access)
    print(new_file_path)
    return new_file_path

def conversion_log_modify(name, input, output, format):
    global conversion_log
    file_stat = os.stat(input)
    print(file_stat)
    print(name)
    creation_time = file_stat.st_mtime
    # Convert to a human-readable format
    readable_time = time.ctime(creation_time)
    print(f"The file was created on: {readable_time}")
    print(f"Original Format: {format}")
    current_time_seconds = time.time()
    local_time = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime(current_time_seconds))
    conversion_log = pd.concat([conversion_log, pd.DataFrame([{
                        'File Name': name,
                        'Original Path': input,
                        'New Path': output,
                        'File Conversion': format,
                        'Original File Created': readable_time,
                        'New File Created': local_time,
                    }])], ignore_index=True)

def convert_files(folder_path):

    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return
    global conversion_log
    contents = os.listdir(folder_path)
    
    for content in contents:
        
        content_path = os.path.join(folder_path, content)
        
        if os.path.isdir(content_path):
            print(f"Entering subfolder: {content_path}")
            create = content_path.replace("preservation", "access/nearline")
            os.makedirs(create,mode=0o775, exist_ok=True)
            convert_files(content_path)
        else:
            print("Found file:", content_path)
            
            if(content.endswith('.ws') or content.endswith('.WS')):
                try: 
                    
                    input_file = content_path
                    # new_name=content.replace('.', '_')
                    # new_file_path = os.path.join(content_path, new_name)
                    # os.rename(content_path, new_file_path)
                    output_file_name = f'{content}.md'
                    output_pdf_name = f'{content}.pdf'
                    folder_path = os.path.dirname(content_path)
                    output_file = os.path.join(folder_path, output_file_name)
                    output_file_pdf = os.path.join(folder_path, output_pdf_name)
                    output_file = transform_file_path(output_file)
                    
                    output_file_pdf = transform_file_path(output_file_pdf)
                    text_mode = False  # Set to True if you want unformatted (text) output
                    print("op md:",output_file)
                    print("op pdf:",output_file_pdf)
                    output_file_md = os.path.join(output_file, output_file_name)
                    output_file_pdf = os.path.join(output_file, output_pdf_name)
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
                    with open(output_file_md, "wt") as outfile:
                        outfile.write(outstring)
                    
                    print("Conversion ready, " + output_file_md + " written!")
                    convert_md_to_pdf(output_file_md, output_file_pdf)
                    conversion_log_modify(content, input_file, output_file_pdf, 'WordStar to PDF')
        
                except Exception as E:
                    print(E)
                    print("Could not convert!")

            elif(content.endswith('.mac') or content.endswith('.MAC') or content.endswith('.doc') or content.endswith('.DOC')):
                try: 
                        
                    input_file = content_path
                    name = content.replace('.mac', '')
                    name = name.replace('.MAC', '')
                    name = content.replace('.doc', '')
                    name = name.replace('.DOC', '')
                    output_file_name = f'{name}.pdf'
                    folder_path = os.path.dirname(content_path)
                    output_file = os.path.join(folder_path, output_file_name)
                    output_file = transform_file_path(output_file)
                    output_file_pdf = os.path.join(output_file, output_file_name)
                    print(output_file)
                    convert_mac(input_file, output_file_pdf)
                    conversion_log_modify(content, input_file, output_file_pdf, 'MacWrite to PDF')
            
                except Exception as E:
                    print(E)
                    print("Could not convert!")
            
            elif(content.endswith('.wpd') or content.endswith('.WPD')):
                try: 
                        
                    input_file = content_path
                    name = content.replace('.wpd', '')
                    name = name.replace('.WPD', '')
                    output_file_name = f'{name}.pdf'
                    folder_path = os.path.dirname(content_path)
                    output_file = os.path.join(folder_path, output_file_name)
                    output_file = transform_file_path(output_file)
                    output_file_pdf = os.path.join(output_file, output_file_name)
                    print(output_file)
                    convert_wpd_to_pdf(input_file, output_file_pdf)
                    conversion_log_modify(content, input_file, output_file_pdf, 'WordPerfect to PDF')
            
                except Exception as E:
                    print(E)
                    print("Could not convert!")
                    
            elif(content.endswith('.wk1') or content.endswith('.WK1')):
                try: 
                        
                    input_file = content_path
                    name = content.replace('.wk1', '')
                    name = name.replace('.WK1', '')
                    output_file_name = f'{name}.xlsx'
                    folder_path = os.path.dirname(content_path)
                    output_file = os.path.join(folder_path, output_file_name)
                    output_file = transform_file_path(output_file)
                    output_file_xl = os.path.join(output_file, output_file_name)
                    print(output_file)
                    convert_to_xlsx(input_file, output_file_xl)
                    conversion_log_modify(content, input_file, output_file_xl, 'Lotus 1-2-3 Spreadsheets to Excel Spreadsheet')
            
                except Exception as E:
                    print(E)
                    print("Could not convert!")

            elif(content.endswith('.wav') or content.endswith('.WAV')):
                try: 
                        
                    input_file = content_path
                    name = content.replace('.wav', '')
                    name = name.replace('.WAV', '')
                    output_file_name = f'{name}.mp3'
                    folder_path = os.path.dirname(content_path)
                    output_file = os.path.join(folder_path, output_file_name)
                    output_file = transform_file_path(output_file)
                    output_file_mp3 = os.path.join(output_file, output_file_name)
                    #print(output_file)
                    convert_wav_to_mp3(input_file, output_file_mp3)
                    conversion_log_modify(content, input_file, output_file_mp3, 'WAV to MP3')
            
                except Exception as E:
                    print(E)
                    print("Could not convert!")

# WordStar Only Functions

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

# MacWrite
def convert_mac(input_file, output_file):
    try:
        subprocess.run(["python", unoconv_path, "-f", "pdf", "-o", output_file, input_file], check=True)
        print("Conversion successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        
# Lotus 1-2-3 Charts to Excel Spreadsheet
def convert_to_xlsx(input_file, output_file):
    try:
        subprocess.run(["python", unoconv_path, '-f', 'xlsx', '-o', output_file, input_file], check=True)
        print(f"Successfully converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting file: {e}")
        
def convert_wpd_to_pdf(input_path, output_path):
    try:
       
        if not output_path.lower().endswith(".pdf"):
            raise ValueError("Output file must have a .pdf extension.")

        # Check if unoconv is installed
        subprocess.run(["python", unoconv_path, "-f", "pdf", "-o", output_path, input_path], check=True)
        print(f"Conversion successful: {input_path} -> {output_path}")
        

    except Exception as e:
        print(f"Conversion failed: {e}")
        
def convert_wav_to_mp3(input_file, output_file, target_sr=44100):
    data, samplerate = sf.read(input_file)
    # Resample the audio data if the sample rate is not supported
    if samplerate != target_sr:
        num = target_sr
        den = samplerate
        data = resample_poly(data, num, den)
        samplerate = target_sr
    sf.write(output_file, data, samplerate, format='mp3')

path1 = r"C:\Users\pal10\Desktop\testcollection - Copy\preservation"

conversion_log = pd.DataFrame(columns=['File Name', 'Original Path', 'New Path', 'File Conversion', 'Original File Created', 'New File Created'])
path2 = path1.replace('preservation','ObjectDocumentation')
os.makedirs(path2,mode=0o775, exist_ok=True)

convert_files(path1)

currenttime = time.localtime()
dateconverted = time.strftime("%Y%m%d%H%M%S", currenttime)
csv_path = os.path.join(path2, f'Conversion_Log_{dateconverted}.csv')
print(csv_path)
conversion_log.to_csv(csv_path, index=False)
                    
                