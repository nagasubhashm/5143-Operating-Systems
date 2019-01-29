import sys

"""
Params:
  pattern [string] - search pattern
  file(s) [string] - name of file or files (directory or wildcard pattern)
"""
def grep(pattern, filename):
    colours={"default":"",
         "blue":   "\x1b[01;34m",
         "cyan":   "\x1b[01;36m",
         "green":  "\x1b[01;32m",
         "red":    "\x1b[01;05;37;41m"}

    noColor = "\x1b[00m"

    # creates a list with one line per entry
    lines = open(filename).readlines()
    for line in lines:
        location = line.find(pattern)
        if location > 0:
            sys.stdout.write(line[:location])
            sys.stdout.write(colours['red']+pattern+noColor)
            sys.stdout.write(line[location+len(pattern):])

def greperror():
    pass

def grepusage():
    print("Usage: grep pattern file[s]...")