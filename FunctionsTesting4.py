import os
import sys
import time
import logging

logging.basicConfig(filename='FunctionsTesting4Results.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def FileDetails():
    logging.info('**Grab the file provided by user as command line argument and show its details**')
    file = sys.argv[1]
    result = os.stat(file)
    print(
        'User id for file is ' + str(result.st_uid) +
        '\n Group id for file is ' + str(result.st_gid) +
        '\n File created on ' + str(time.ctime(result.st_ctime)) +
        '\n last modified on ' + str(time.ctime(result.st_mtime)) +
        '\n last accessed on ' + str(time.ctime(result.st_atime))
    )
    logging.info(
        'User id for file is ' + str(result.st_uid) +
        '\n Group id for file is ' + str(result.st_gid) +
        '\n File created on ' + str(time.ctime(result.st_ctime)) +
        '\n last modified on ' + str(time.ctime(result.st_mtime)) +
        '\n last accessed on ' + str(time.ctime(result.st_atime))
    )
    print('\n\n')
    logging.info('\n\n')

    #In existing directory, create new directories recursively and change working directory to last dir in the hirrarchy
    logging.info('**show current wd, create new dir recursively, change cwd and show path again**')
    cwd = os.getcwd()
    print('Before creating directories, cwd is: ' + cwd)
    logging.info('Before creating directories, cwd is: ' + cwd)
    new_directories_path = './new0/new1/new2/new3'
    os.makedirs(new_directories_path)
    os.chdir(cwd + new_directories_path[1:len(new_directories_path)])
    print('After creating directories and changing dir path, cwd is: ' + os.getcwd())
    logging.info('After creating directories and changing dir path, cwd is: ' + os.getcwd())

    #remove last directory and then print cwd
    os.rmdir(os.getcwd())
    time.sleep(5)
    print('After deleting the last dir cwd is: ' + os.getcwd())
    logging.info('After deleting the last dir, cwd is: ' + os.getcwd())

FileDetails()

# to run, on terminal navigate to files location and then..
# python FunctionsTesting4.py 'file_name'