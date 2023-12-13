import subprocess
import os
import sys
import shutil

def convert_doc_to_pdf(doc_path, pdf_path):
    try:
        subprocess.run(["python", r"C:\Users\pal10\AppData\Roaming\Python\Python312\Scripts\unoconv", "-f", "pdf", "-o", pdf_path, doc_path], check=True)
        print("Conversion successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        
def find_subfolder(start_path):
    # Check if the specified path exists
    if not os.path.exists(start_path):
        print(f"Path {start_path} does not exist.")
        return []

    root_contents = os.listdir(start_path)

    for content in root_contents:
        content_path = os.path.join(start_path, content)
        # new_path = os.path.join(os.path.dirname(folder_path), content)
        content_name = content.replace('.doc', '')
        pdf_path = fr'{start_path}\\{content_name}.pdf'
        print(content_path)
        print(pdf_path)
        convert_doc_to_pdf(content_path, pdf_path)
        
start_path = r'C:\Users\pal10\Desktop\Nora\preservation2' 
find_subfolder(start_path)