import os
import sys

#Note: os.scandir() works on python 3.5

def UseScanDirFun():
    #uncomment the below instruction when using python 3.5 and above
    #path = sys.argv[1]

    #comment the below instruction when using python 3.5 and above
    path = '/Users/ts/Documents/resources/pythonPractise/'

    result = os.scandir(path)
    for item in result:
        if item.is_dir():
            type = 'directory'
        elif item.is_file():
            type = 'file'
        elif item.is_symlink():
            type = 'link'
        else:
            type = 'unknown'
        print(str(item.name) + ' is a ' + type)

UseScanDirFun()

#on line 11, replace path variable value to any directory