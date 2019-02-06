#!/usr/bin/env python
from subprocess import call

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