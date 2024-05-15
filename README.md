# DigiCurationScripts
Repository containing a variety of Python scripts intended to assist with digital curation tasks 

### Setup Visual Studio Code

Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. Use VS Code for running all the scripts in the repository.

**VS Code Download Link:** https://code.visualstudio.com/download

**(Prerequisite) LibreOffice Download Link:** https://www.libreoffice.org/get-help/install-howto/

**Install Python (the latest stable version) on your PC:** https://www.python.org/downloads/

Click on the "Download" link for the most recent release, and from the redirected page choose the Python installer based on your System settings (eg. for a 64-bit Windows PC, pick the "Windows installer (64-bit)" option.) 

Also, keep track of the folder in which Python is installed in your PC. The path to this folder may be required to run some of the scripts in this repository. In a Windows PC, it typically gets installed under Disk C > Users > (username) > AppData > Roaming (eg., C:\Users\pal10\AppData\Roaming\Python\Python312) 

**VS Code Python extension:**

Go to the extensions section in VS Code (highlighted icon in the sidebar).

![Image 1](images/Picture1.png)

![Image 2](images/Picture2.png)

### Some Common Python Libraries

Keeping some commonly used Python libraries installed in your PC before running the scripts might be useful. Navigate to "Command Prompt" on your PC, and run the following commands to install the Python libraries:

```bash
pip install pandas
```

```bash
pip install setuptools
```

```bash
pip install unoconv
```

### Cloning the GitHub repository:

On the main branch of the repository, click on the green 'Code' button, and then 'Download ZIP Folder':

![Image 3](images/DownloadRepo.png)

Once you download all the files in the repository to your PC, extract all the files to a designated folder in your PC to create a local copy of the repository (right click on the ZIP folder > "Extract All"). Launch VS Code and go to File > Open Folder (top left) and then open up the folder on VS Code:

![Image 4](images/PythonCode.png)

Navigate to the Python script you wish to test/run. Make sure that the name of the file ends with ".py" (eg. as illustrated above, macwriteconv.py)

To run a script, click on the triangle icon at the top right corner of the screen of the VS Code Editor:

![Image 5](images/RunCode.png)

