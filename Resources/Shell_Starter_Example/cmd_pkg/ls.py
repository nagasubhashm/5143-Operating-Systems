#!/usr/bin/env python
from subprocess import call
from subprocess import check_output
import glob
import os

def ls(**kwargs):
    # Params key exist
    if 'params' in kwargs:
        params = kwargs['params']

        # Makes sure params is a list and has min 1 value
        if isinstance(params, (list,)) and len(params) > 0:
            dir = params[0]
        else:
            dir = os.getcwd()
    else:
        dir = os.getcwd()

    # grab directory listing of current directory
    files = glob.glob(dir + os.path.sep+'*')

    # sort files alphabetically (for now)
    files = sorted(files)

    rows, columns = os.popen('stty size', 'r').read().split()
    print(rows,columns)

    # string return value
    retValue = ""

    # create a string of files to return
    for filename in files:
        filename = filename.split('/')
        retValue += filename[-1] + "\t"

    return retValue.strip() # clear off last newline

ls.__doc__="""
ls : Directory listing
"""

if __name__=='__main__':
    print(ls())
