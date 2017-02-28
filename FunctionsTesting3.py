import os

def ChangeCurrentDirectories():
    print('Present working directory is: ' + str(os.getcwd()))
    #Moving one level up in the hierarchy
    os.chdir(os.pardir)
    print('After moving, present working directory is: ' + str(os.getcwd()))

ChangeCurrentDirectories()

