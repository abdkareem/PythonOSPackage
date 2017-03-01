import os
import sys
import logging

logging.basicConfig(filename='FunctionsTesting2Results.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

#Note: os.scandir() works on python 3.5

def UseScanDirFun():
    #uncomment the instruction on line 12 when using python interpreter version 3.5 or above
    #and run the program as   $python FunctionsTesting2.py /*Your_PATH*/
    #path = sys.argv[1]

    #comment the below instruction when using python interpreter version 3.5 or above
    path = '/Users/ts/Documents/resources/pythonPractise/'

    logging.info('**Scan the path provided by user and list whether it\'s entries are Directory or File**')
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
        logging.info(str(item.name) + ' is a ' + type)

UseScanDirFun()

#on line 15, replace path variable value to any directory