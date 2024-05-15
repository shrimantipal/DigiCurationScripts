import os
import subprocess

def install_packages():
    command = "pip install tk weasyprint markdown2 pandas scipy soundfile"
    
    # For Windows
    if os.name == 'nt':
        subprocess.run(['cmd', '/c', command])
    # For Unix-like systems (Linux, macOS)
    else:
        subprocess.run(['bash', '-c', command])

if __name__ == "__main__":
    install_packages()
