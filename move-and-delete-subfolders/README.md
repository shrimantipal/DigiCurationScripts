# Find Directories and Move Content

**The last part of the script is the only part that needs to be modified for each directory that needs to be modified and for each subfolder in the directory that needs to be deleted.**

For multiple subfolders in the same directory to be deleted, the ‘start_path’ variable remains the same.

Eg. In the case of the ‘GreatAmericanPeopleShow\preservation’ directory:

Since in the given directory structure for ‘GreatAmericanPeopleShow\preservation’, we want to delete the \[root] subfolder and the 001 subfolder, we have to run the code twice. The start_path remains the same, i.e.: ‘Z:\IHLC\GreatAmericanPeopleShow\preservation’ (the BornDigital drive is mapped to the Z drive in this case). 

First we assign the value ‘\[root]’ to the variable move_up to delete all the \[root] subfolders in the directory structure and move all its contents up one level. Then, we assign the value ‘001’ (move_up = ‘001’) to the variable, so all the contents of 001 get moved up one level.

So first:

```
start_path = r'Z:\IHLC\GreatAmericanPeopleShow - Copy\preservation' 
move_up = '[root]' # the folder that needs to be deleted. 
find_subfolder(start_path, move_up)
```

And then:

```
start_path = r'Z:\IHLC\GreatAmericanPeopleShow - Copy\preservation' 
move_up = '001' # the folder that needs to be deleted. 
find_subfolder(start_path, move_up)
```

**The code can be called as many times as required by just changing the move_up variable name to delete whichever subfolders are needed to be deleted.**

The function 'find_subfolder' traverses through the directory structure to find a certain subfolder that needs to be deleted (e.g. ‘\[root]’ or ‘001’, as required for this particular use case). If the subfolder exists, then it calls the function ‘move_subfolders_up’ which handles the transferring of contents from the target subfolder to one level above it and deletes the subfolder. The path of the subfolder to be deleted is sent as the argument to this function. 

The function ‘move_subfolders_up’ moves all the files and folders in the subfolder to be deleted up one level.
