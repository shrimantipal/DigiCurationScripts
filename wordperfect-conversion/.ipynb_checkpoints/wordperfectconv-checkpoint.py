import pandas as pd
import os
import subprocess

df = pd.read_csv('gaps_profile.csv')
print(df.head())

def convert_wpd_to_pdf(input_path, output_path):
    try:

        # if not input_path.lower().endswith(".wpd"):
        #     raise ValueError("Input file must have a .wpd extension.")

        # Ensure the output file has a .pdf extension
        if not output_path.lower().endswith(".pdf"):
            raise ValueError("Output file must have a .pdf extension.")

        # Check if unoconv is installed
        subprocess.run(["python", r"C:\Users\pal10\AppData\Roaming\Python\Python312\Scripts\unoconv", "-f", "pdf", "-o", output_path, input_path], check=True)

        # unoconv_path = r"C:\Users\pal10\AppData\Roaming\Python\Python312\Scripts\unoconv"  # You may need to provide the full path to unoconv
        # subprocess.run([unoconv_path, "--version"], check=True)

        # Convert .wpd to .pdf using unoconv
        # subprocess.run([unoconv_path, "-f", "pdf", "-o", output_path, input_path], check=True)

        print(f"Conversion successful: {input_path} -> {output_path}")
        

    except Exception as e:
        print(f"Conversion failed: {e}")
        

def transform_file_path(file_path):
    # Split the file path into components
    components = file_path.split(os.sep)
    
    # Find the index of 'preservation'
    preservation_index = components.index('preservation')
    
    # Replace 'preservation' with 'access\nearline'
    components[preservation_index] = r"access\nearline"
    
    # Join the components back into a file path
    new_file_path = os.sep.join(components[:-1])  # Remove the last directory
    
    return new_file_path

for index, row in df.iterrows():
    
    if(row['FORMAT_NAME'] == "WordPerfect for MS-DOS/Windows Document"):
        input_path = row['FILE_PATH']
        filename = os.path.basename(input_path)
        directory_path = os.path.dirname(input_path)
        if(".wpd" in filename):
            output_file = filename.replace(".wpd", ".pdf")
        else:
            output_file = fr"{filename}.pdf"
            print(output_file)
        output_directory = transform_file_path(directory_path)
        output_path = os.path.join(output_directory, output_file)
        copied_path = os.path.join(output_directory, filename)
        print(output_path)
        convert_wpd_to_pdf(input_path, output_path)
