import os
import sys
import time

def FileDetails():
    file = sys.argv[1]
    result = os.stat(file)
    print(
        'User id for file is ' + str(result.st_uid) +
        '\n Groud id for file is ' + str(result.st_gid) +
        '\n File created on ' + str(time.ctime(result.st_ctime)) +
        '\n last modified on' + str(time.ctime(result.st_mtime)) +
        '\n last accessed on' + str(time.ctime(result.st_atime))
    )
    print('\n\n\n')

    #In existing directory, create new directories recursively and change working directory to last dir in the hirrarchy
    cwd = os.getcwd()
    print('Before creating directories, cwd is: ' + cwd)
    new_directories_path = './new0/new1/new2/new3'
    os.makedirs(new_directories_path)
    os.chdir(cwd + new_directories_path[1:len(new_directories_path)])
    print(os.getcwd())
    print('After creating directories and changing, cwd is: ' + os.getcwd())

    #remove last directory and then print cwd
    os.rmdir(os.getcwd())
    time.sleep(5)
    print('After deleting the last dir cwd is: ' + os.getcwd())

FileDetails()

# to run, on terminal navigate to files location and then..
# python FunctionsTesting4.py 'file_name'