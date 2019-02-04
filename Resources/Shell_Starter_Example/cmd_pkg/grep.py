import sys

def greperror():
    pass

def grepversion():
    """
    grep (GZSH grep) 1.0-FreeBSD")
    """
    pass

def grepusage():
    """
    usage: grep [-abcDEFGHhIiJLlmnOoqRSsUVvwxZ] [-A num] [-B num] [-C[num]]
        [-e pattern] [-f file] [--binary-files=value] [--color=when]
        [--context[=num]] [--directories=action] [--label] [--line-buffered]
        [--null] [pattern] [file ...]
    """
    pass

def grep(**kwargs):
    """
    GREP                         User Commands                        GREP
    NAME
        grep - print lines that match patterns
    SYNOPSIS
        grep [OPTION...] PATTERNS [FILE...]
        grep [OPTION...] -e PATTERNS ... [FILE...]
        grep [OPTION...] -f PATTERN_FILE ... [FILE...]
    DESCRIPTION
        grep searches for PATTERNS in each FILE.  PATTERNS is one or patterns
        separated by newline characters, and grep prints each line that
        matches a pattern.

        A FILE of "-" stands for standard input.  If no FILE is given,
        recursive searches examine the working directory, and nonrecursive
        searches read standard input.
    OPTIONS
        Generic Program Information
            --help Output a usage message and exit.

            --version
                    Output the version number of grep and exit.
    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'flags' in kwargs:
        flags = kwargs['flags']

    if 'v' in flags or 'version' in flags:
        print(grepversion.__doc__)
        return

    if not len(params) == 2:
        print(grepusage.__doc__)
        return
    else:
        pattern = params[0]
        filename = params[1]

    colours={"default":"",
         "blue":   "\x1b[01;34m",
         "cyan":   "\x1b[01;36m",
         "green":  "\x1b[01;32m",
         "red":    "\x1b[01;31m",
         "magenta": "\x1b[01;35m",
         "white": "\x1b[01;37m"}

    noColor = "\x1b[00m"

    result = ""

    # creates a list with one line per entry
    lines = open(filename).readlines()
    line_num = 1
    for line in lines:
        location = line.find(pattern)
        if location > 0:
            # show line numbers
            if 'n' in flags:
                result += str(line_num)+":"
            result += line[:location] + colours['red']+pattern+noColor + line[location+len(pattern):]
        line_num += 1

    return result