# MacWrite File Conversion (.doc to .pdf)

## Installations
- Python (3.12+)
- Unoconv Package

**Universal Office Converter (unoconv)** is a command-line tool to convert any document format that LibreOffice can import to any document format that LibreOffice can export. The Python package for unoconv needs to be installed for the conversion script to work.

Go to Command Prompt and run the following: 

```bash
pip install unoconv
```

You must navigate to the folder where Python is installed in your PC (this varies, but on Windows is typically under Users > Username > AppData > Roaming). Under the “Scripts” folder where Python is installed in your machine, there should be a file named “unoconv”. **We need to note the path of this file and use it in the convert_doc_to_pdf function in the script.** In this particular case, the file path is as follows: 
C:\Users\pal10\AppData\Roaming\Python\Python312\Scripts\unoconv

In the script, find the “start_path” variable and replace it with the path of the folder containing the MacWrite files. This variable is located towards the very end of the script. Once this is done, run the script.
