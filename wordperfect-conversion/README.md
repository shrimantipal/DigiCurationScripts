# WordPerfect File Conversion

## For the folder containing the WordPerfect files, you must generate a DROID file identification report first, and save the report as a CSV.

## Installations
- Python (3.12+)
- Unoconv Package (refer to MacWrite conversion documentation regarding Unoconv package installation)
- pandas
- DROID File Identification Tool: https://www.nationalarchives.gov.uk/information-management/manage-information/preserving-digital-records/droid/

To install the pandas library, open up Command Prompt on Windows, and run the following command:

```bash
pip install pandas
```

To install Unoconv, run the following command on Command Prompt:

```bash
pip install unoconv
```
You must navigate to the folder where Python is installed in your PC (this varies, but on Windows is typically under Users > Username > AppData > Roaming). Under the “Scripts” folder where Python is installed in your machine, there should be a file named “unoconv”. **We need to note the path of this file and use it in the convert_wpd_to_pdf function in the script.** In this particular case, the file path is as follows: 
C:\Users\pal10\AppData\Roaming\Python\Python312\Scripts\unoconv

Find the file named "unoconv" in the Scripts folder where Python is installed, right click the file, and click on "Copy as Path" to copy the path.

You need to add the path of this file to the function convert_wpd_to_pdf:

```python

def convert_wpd_to_pdf(input_path, output_path):
    try:
        # if not input_path.lower().endswith(".wpd"):
        #  raise ValueError("Input file must have a .wpd extension.")
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


```

In the first line after the import statements in the script, modify the name of the DROID file identification report according to what you have saved it in your PC. In this case, it is saved as "gaps_profile.csv":

```python
df = pd.read_csv('gaps_profile.csv')
```

