import os
import logging

logging.basicConfig(filename='FunctionsTesting3Results.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def ChangeCurrentDirectories():
    logging.info('**Show current wd and then move a level up in the hierarchy and show the current wd again**')
    print('Present working directory is: ' + str(os.getcwd()))
    logging.info('Current working directory is: ' + str(os.getcwd()))
    #Moving one level up in the hierarchy
    os.chdir(os.pardir)
    print('After moving a level up, current working directory is: ' + str(os.getcwd()))
    logging.info('After moving a level up, current working directory is: ' + str(os.getcwd()))

ChangeCurrentDirectories()

