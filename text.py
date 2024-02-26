import os
import shutil

path = "C:\\Users\\DELL\\Documents\\text.txt"

if os.path.exists(path):
    print('this location exist')

if os.path.isfile(path):
    print('this location is a file')

elif os.path.isdir(path):
    print('this location is a directory')

else:
    print('the location doesn\'t exist')