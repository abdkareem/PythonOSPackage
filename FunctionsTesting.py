import os
import sys
import logging

logging.basicConfig(filename='FunctionsTestingResults.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def ListFiles():
    """
    1) list all the files and directories in the path provided by user as command line argument.
    each name must be in a new line.

    2) using the path from 1) list files recursively i.e. files within its sub-directories
    """
    #1)
    logging.info('**Show path provided by user and list its contents**')
    path = sys.argv[1]
    print('The path passed is: ' + str(path))
    logging.info('The path passesd is: ' + str(path))
    files = os.listdir(path)
    for name in range(len(files)):
        print('File at index ' + str(name) + ' is ' + str(files[name]))
        logging.info('File at index ' + str(name) + ' is ' + str(files[name]))
    print('\n\n')
    logging.info('\n\n')

    #2)
    logging.info('**List contents of sub-directories within the path provided by user**')
    for directory, subdirectory, files in (os.walk(path)):
        print(directory)
        logging.info(directory)
        subdirectory = [n + '/' for n in subdirectory]
        contents = subdirectory + files
        # see how the output appears when you comment out 34 and 36
        for content in contents:
            print(content)
            logging.info(content)


ListFiles()

# to run file, navigate to files location on terminal, then..
# python FunctionsTesting.py /yourpath/