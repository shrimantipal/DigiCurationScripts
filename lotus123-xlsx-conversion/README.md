# Lotus 1-2-3 to Excel Spreadsheet File Conversion


## Installations
- Python (3.12+)
- LibreOffice
- Python libraries: xlrd, openpyxl

To install the required Python libraries, open up Command Prompt on Windows, and run the following commands (one after the other):

```bash
pip install  xlrd
```

```bash
pip install  openpyxl
```

Copy the path of the folder containing the Lotus files (should be a preservation folder path).

Note that the files get saved to respective [barcode] subfolders in access/nearline, so make sure you run the directory duplication script first.

Navigate to the 'start_path' variable towards the end of the code. Change it to the folder path containing the Lotus files.

### Data loss: Any charts present in the original Lotus 1-2-3 spreadsheet will probably not be saved in the Excel spreadsheet.


