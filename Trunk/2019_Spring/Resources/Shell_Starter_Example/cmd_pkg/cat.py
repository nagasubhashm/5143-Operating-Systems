#!/usr/bin/env python
from subprocess import call

<<<<<<< HEAD
cat('params'=['README.md','bacons.txt'],'flags'=[] 'appendfile'='outname.txt')

def cat(**kwargs):
    string_Files = ""
    if 'params' in kwargs:
        if len(kwargs['params'] == 0):
            catusage()
            return
        else:
            for f in kwargs['params']:
            f = open(f,'r').read()

            return string_Files

    call(["cat", file])
=======


def cat(**kwargs):
    """   
    NAME
        cat - concatenate files and print on the standard output
    SYNOPSIS
        cat [OPTION]... [FILE]...
    DESCRIPTION
        Concatenate FILE(s) to standard output.

        -A, --show-all
                equivalent to -vET

        -b, --number-nonblank
                number nonempty output lines, overrides -n

        -e     equivalent to -vE

        -E, --show-ends
                display $ at end of each line

        -n, --number
                number all output lines

        -s, --squeeze-blank
                suppress repeated empty output lines

        -t     equivalent to -vT

        -T, --show-tabs
                display TAB characters as ^I

        --help display this help and exit

        --version
                output version information and exit
    EXAMPLES
        cat f - g
                Output f's contents, then standard input, then g's contents.

        cat    Copy standard input to standard output.
    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'flags' in kwargs:
        flags = kwargs['flags']
    command = ["cat"]

    for f in params:
        command.append(f)

    call(command)
>>>>>>> 5f181e36c8fb60184acd516f4a439b625b540e15
