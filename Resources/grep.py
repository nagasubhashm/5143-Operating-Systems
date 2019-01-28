import os,sys

colours={"default":"",
         "blue":   "\x1b[01;34m",
         "cyan":   "\x1b[01;36m",
         "green":  "\x1b[01;32m",
         "red":    "\x1b[01;05;37;41m"}

noColor = "\x1b[00m"

lines = open('bacon.txt').readlines()

phrase = 'bacon'

for line in lines:
    location = line.find(phrase)
    if location >= 0:
        sys.stdout.write(line[:location])
        sys.stdout.write(colours['cyan']+phrase+noColor)
        sys.stdout.write(line[location+len(phrase):])
