"""" 

The glob library in Python is used to find files and directories whose names match a pattern, 
similar to how wildcard matching works in a terminal or file explorer.

"""
import glob

myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        data = file.readline()
        print(f"FilePath: {filepath} \n {data}")