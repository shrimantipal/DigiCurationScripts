### PIC to JPG Conversion Script

This Python script converts .PIC files to .jpg files. The .PIC files used for testing this script were originally Lotus 1-2-3 Charts.

#### Tools Required: GraphicConverter

#### Installing GraphicConverter for your system:

GraphicConverter is an image editing and conversion software for MacOS (not available on Windows). Download the software here (use the link in the "Test for Free" section): https://www.lemkesoft.de/en/products/graphicconverter

* GraphicConverter is shareware. That means you can test the product free of charge and without any obligations before you purchase it.

Make sure the latest version of Python is installed.

Once GraphicConverter is installed in your system, you can run the script. Before you run the script, make sure to modify the start_path variable to the path of the preservation containing the PIC files. Once the script starts running, it will duplicate the directory structure of the preservation folder in access/nearline and then store the output .JPG files from the conversions in the designated subfolder.

```python
start_path = r'/Users/pal10/Desktop/testcollection/preservation' 
find_subfolder(start_path)
```
