import os
import sys

def ListFiles():
    """
    1) list all the files and directories in path. path provided by user as command line argument
    each name must be in a new line.

    2) list files recursively i.e. files within its sub-directories
    """
    #1)
    path = sys.argv[1]

    print('The path passed is: ' + str(path))
    files = os.listdir(path)
    for name in range(len(files)):
        print('File at index ' + str(name) + ' is ' + str(files[name]))
    print('\n\n\n')

    #2)
    for directory, subdirectory, files in (os.walk(path)):
        print(directory)
        subdirectory = [n + '/' for n in subdirectory]
        contents = subdirectory + files
        # see how the output appears when you comment out 34 and 36
        for content in contents:
            print(content)


ListFiles()

# to run file, navigate to files location on terminal, then..
# python FunctionsTesting.py /yourpath/