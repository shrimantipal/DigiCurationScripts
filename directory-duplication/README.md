## Duplicate the directory structure of a folder in another folder.

### Example: the subfolder "preservation" contains multiple subfolders that are named after barcode numbers, all of which contain subfolders as well. The objective is to copy all the barcode subfolders in a subfolder called "nearline" of the folder "access" which is at the same level as the "preservation" folder, without copying the contents of the barcode subfolders.


The variable start_path contains the path of the folder whose directory contents need to be duplicated. 

```python
start_path = r'C:/Users/pal10/Desktop/GAPSFiles/GAPSTestsetCopy/preservation'
```

Change this variable to whichever path you want to copy the structure of the duplicate variable. Running the script will create a duplicate directory structure of the preservation folder in the access/nearline folder.

