### PIC to JPG Conversion Script

This Python script converts .PIC files to .jpg files. The .PIC files used for testing this script were originally Lotus 1-2-3 Charts.

#### Tools Required: GraphicConverter

#### Installing GraphicConverter for your system:

GraphicConverter is an image editing and conversion software for MacOS (not available on Windows). Download the software here (use the link in the "Test for Free" section): https://www.lemkesoft.de/en/products/graphicconverter

* GraphicConverter is shareware. That means you can test the product free of charge and without any obligations before you purchase it.

Make sure the latest version of Python is installed.

#### Once GraphicConverter is installed in your system, find the software in the "Applications" page of your Mac. Follow the steps below to copy the path to the application:

1. Right click or Control+click on the icon, and from the options, select "Show Package Contents". 
2. You should see a folder labelled "Contents" - click on it.
3. You should see more subfolders after Step 2. Click on the subfolder named "MacOS".
4. Inside "MacOS", you should see a file named "GraphicConverter 12" (or whichever version of GraphicConverter you have installed). Ctrl + click on it. Once you see the options, click on "Get Info".
5. Under "Get Info", you should see the location of the file listed under "Where". (eg. Where: /Applications/GraphicConverter 12.app/Contents/MacOS). Ctrl + click on this line, and select the option "Copy as pathname"
6. Make sure you also take note of the file name as well. (eg. GraphicConverter 12). You must know which version of GraphicConverter you are running.
7. In the script, navigate to the convert_to_jpg function. On line 41, (below the line where the command begins), replace the existing file path with your file path. That is, replace "/Applications/GraphicConverter 12.app/Contents/MacOS/GraphicConverter 12" with your path to the GraphicConverter application file.
8. Make sure the path ends with the file name, i.e., GraphicConverter 12 (or whichever version is installed in your system)

Make sure to modify the start_path variable to the path of the preservation containing the PIC files. This is the variable that needs to be modified:

```python
start_path = r'/Users/pal10/Desktop/testcollection/preservation' 
find_subfolder(start_path)
```
After these changes are made, run the script. Once the script starts running, it will duplicate the directory structure of the preservation folder in access/nearline and then store the output .JPG files from the conversions in the designated subfolder.
