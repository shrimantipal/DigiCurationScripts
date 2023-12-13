### WordStar Conversion Script

This Python script converts .ws files to .md format first (by sequentially converting each character in the .ws file) and then into .pdf format (using WeasyPrint and Markdown2).

Original code for converting a .ws file to markdown format. (Modifications were required to convert files to .pdf format in bulk located in nested directories).

#### Dependencies: WeasyPrint, Markdown2, GTK3

####Installing WeasyPrint for your system:

WeasyPrint is used for converting Markdown files (or other file formats) to PDFs. Only Windows 11 64-bit is supported. 

Make sure the latest version of Python is installed. Then, download the latest GTK3 installer (https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases) and launch it. If you don’t know what some options mean, you can safely keep the default options selected.

You can then install WeasyPrint in a virtual environment using pip (using Command Prompt):

```bash
python3 -m venv venv
venv\Scripts\activate.bat
python3 -m pip install weasyprint
python3 -m weasyprint –info
```

If using ‘python3’ throws an error, try using ‘python’ instead.
Refer to the detailed WeasyPrint installation guide here: 

https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows

WeasyPrint Python packages (run on Command Prompt):
```bash
pip install weasyprint markdown2
```
The script reads the contents of each .ws file character by character and converts it to a readable format. (Note that this does result in some data loss for special characters.)

The script works given all the WordStar files that need to be converted are stored in subfolders of the same name in any nested directory structure. In this case, the WordStar files are all located in subfolders called “OriginalFiles”. The start_path variable contains the root folder of the nested directory, and we iterate into every OriginalFiles subfolder to convert the WordStar files. 

```python
start_path = r'C:\Users\pal10\Desktop\WSTestSet\preservation' 
find = 'OriginalFiles' 
find_subfolder(start_path, find)
```

**Additional information:** WordTsar (http://wordtsar.ca/downloads/) is an open-source WordStar clone for the 21st century. It can open all .ws files in a text-based editor.
