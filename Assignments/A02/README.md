## Shell Project - Implementation of a basic shell.
### Due: Multiple Dates

- Part 1 - Group Selection (posted on Slack) - Due: Jan 28<sup>th</sup> 
- Part 2 - Repository Creation (link posted on Slack) - Due: Jan 30<sup>th</sup> 
- Part 3 - Small Working Example - Due: Feb 11<sup>th</sup>
- Part 4 - Final Product - Due: Feb 18<sup>th</sup>
- Part 5 - Project Presentations - Feb 18<sup>th</sup> - 20<sup>th</sup>

## Overview

You will be implementing a "shell". We use a shell quite often and should have a grasp on expected shell behavior. Below is a brief overview of top level shell behavior:
- After start-up processing, your program repeatedly should perform these actions:
    - Print to stdout a prompt consisting of a percent sign followed by a space.
    - Read a line from stdin.
    - Lexically analyze the line and create an array of command parts (tokens). 
    - Syntactically analyze (i.e. parse) the token array to form a command.
    - Once identified, the proper command is executed:
        - It creates a child process by duplicating itself.
        - The overloaded process receives all the remaining strings given from a keyboard input (if necessary), and starts a command execution.

### Requirements

- You must use threads to execute each command in a thread.
- You should wait for the thread to complete, before returning control to the main process (unless specified to run in background).
- Your language of implementation will be Python.
- Your shell must support the following types of commands:

>1. The internal shell command "exit" which terminates the shell.
    - **Concepts**: shell commands, exiting the shell
    - **System calls**: `exit()`
2. A command with no arguments
    - **Example**: `ls`
    - **Details**: Your shell must block until the command completes and, if the return code is abnormal, print out a message to that effect.
    - **Concepts**: Forking a child process, waiting for it to complete, synchronous execution
    - **System calls**: `fork()`, `execvp()`, `exit()`, `wait()`
1. A command with arguments
    - **Example**: `ls -l`
    - **Details**: Argument 0 is the name of the command
    - **Concepts**: Command-line parameters 
2. A command, with or without arguments, executed in the background using `&`.
    - For simplicity, assume that if present the `&` is always the last thing on the line.
    - **Example**: `any-command &`
    - **Details**: In this case, your shell must execute the command and return immediately, not blocking until the command finishes.
    - **Concepts**: Background execution, signals, signal handlers, processes, asynchronous execution
    - **System calls**: `sigset()`
3. A command, with or without arguments, whose output is redirected to a file
    - **Example**: `ls -l > foo`
    - **Details**: This takes the output of the command and put it in the named file
    - **Concepts**: File operations, output redirection
    - **System calls**: `freopen()`
4. A command, with or without arguments, whose input is redirected from a file
    - **Example**: `sort < testfile`
    - **Details**: This takes the named file as input to the command
    - **Concepts**: Input redirection, more file operations
    - **System calls**: `freopen()`
5. A command, with or without arguments, whose output is piped to the input of another command.
    - **Example**: `ls -l | more`
    - **Details**: This takes the output of the first command and makes it the input to the second command
    - **Concepts**: Pipes, synchronous operation
    - **System calls**: `pipe()`

>Note: You must check and correctly handle all return values. This means that you need to read the man pages for each function to figure out what the possible return values are, what errors they indicate, and what you must do when you get that error

Additionally, and I shouldn't have to point this out, but implementing a command must be done without making a call to
the existing shell:
```python
from subprocess import call

call(["ls", "-l"])

```
The above implementation of the `ls` command with the `-l` flag, is NOT an implementation. It is a "system" call to the existing shell. I also do not expect your python implementation of the `ls` command to be as extensive as this: http://www.pixelbeat.org/talks/python/ls.py.html . Your implementations should be somewhere in between. 


### Commands To Implement

| Command	     | Flag / Param      | Meaning                           |
|----------------|------------|-----------------------------------|
| `ls	`        |            | list files and directories        |
|                |    `-a`	  |   list all show hidden files      |
|                |    `-l`	  |    long listing                   |
|                |    `-h`	  |    human readable sizes           |
| `mkdir`	     |             |make a directory                  |
| `cd`           |  `directory` |change to named directory         |
| `cd`	         |             |change to home-directory          |
|                |   `~	`      |change to home-directory           |
| 	             |   `..`      |change to parent directory          | 
| `pwd`	         |             |display the path of the current directory |

| Command | Params/Flags      |Meaning                                  |
|---------|-----------|-------------------------------|
| `cp `            | `file1 file2`    | copy file1 and call it file2 |
| `mv`             | `file1 file2`    | move or rename file1 to file2 |
| `rm`             | `file`           | remove a file |
| `rmdir`             | `directory`  | remove a directory |
| `cat`             | `file` | display a file |
|                   | `file1`,`file2`,`fileN` | display each of the files as if they were concatenated |
| `less`             | `file` | display a file a page at a time |
| `head`             | `file` | display the first few lines of a file |
|                    | `-n` | how many lines to display |
| `tail`             | `file` | display the last few lines of a file |
|                    | `-n`| how many lines to display|
| `grep`             | `'keyword' file` | search a file(s) files for keywords and print lines where pattern is found |
|                   | `-l` | only return file names where the word or pattern is found |
| `wc`             | `file` | count number of lines/words/characters in file |
|                  | `-l` | count number of lines in file |
|                  | `-m` | count number of characters in file |
|                  | `-w` | count number of words in file |

| Command | Meaning      |
|--------------------------|---------|
| `command > file`           | redirect standard output to a file |
| `command >> file`          | append standard output to a file |
| ~~`command < file`~~           | ~~redirect standard input from a file~~|
| `command1` | `command2`      | pipe the output of command1 to the input of command2 |
| `cat file1 file2 > file0`  | concatenate file1 and file2 to file0 |
| `sort`                     | sort data |
| `who`                      | list users currently logged in |

| Command | Meaning |
|--------------------------|---------|
| `history`           | show a history of all your commands |
| `!x`                | this loads command `x` from your history so you can run it again |
| `chmod xxx`         | change modify permission | 

>Note: Every command should print out help for the command if the user enters `command --help`. Look at [docstrings](https://realpython.com/documenting-python-code/) as one possible solution.
## Deliverables

***Part 1 - Group Selection***
- Put a message on the course channel (not a direct message to me) with the following format:

>Group Members
>
| Name     | Email   | Github Username |
|----------|---------|-----------------|
| Name 1   | Email.One | username_one  |
| Name 2   | Email.Two | username_two  |
| Name 3   | Email.Three | username_three |

***Part 2***
- Create a private repository on github.
- Invite rugbyprof to be a collaborator.
- Place your group names on the README.md along with a description (see below).
- Even though your shell will have its own private repo, each member must (by the final due date) have a copy on thier course repo:
  - In your `assignments/shell` folder from Part 1. 
  - Create a file called `driver.py` in the `shell` folder.
  - Create a file called `README.md` in your `shell` folder.
  - Additional files are ok, for example if you want to place each "command" in a seperate file for organizational purposes, that would be not only acceptable, but encouraged.

***Part 3 and Part 4***
#### `shell.py`

- This file is where your shell code will exist and be executed from. 
- You should code in a modular format with comments that are commensurate with graduate work.

#### `README.md`

- This file will list pertinant information to include (at a minimum):
- Date
- Project Title
- Project description 
    - With a list of all commands implemented
    - Make a note of any commands that do not work or are not implemented.
    - The documentation of non-working portions of the shell will be viewed favorably by me. 
    - Passing of portions of the shell as working when they don't will affect your grade considerably.
- A references section that cites any sources used to assist your group in creating the shell. 
    - Using some external code is ok as long as you follow the following guidelines:
        - Cite the source of the code in the `README.md` and in the comments of the `shell.py` file. 
        - Only use small portions of external code. 
   - I reserve the right to make any final decisions on whether your group is obtaining too much external help. If your not sure, ask.
- Group Members
- Any instructions necessary to ensure I run your code correctly.


