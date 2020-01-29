## Shell Project - Implementation of a basic shell.
### Due: Multiple Dates

#### Hold until class discussion

- Part 1 - Repository Creation & Repo Creation - Due: Feb 4<sup>th</sup> 
- Part 2 - Small Working Example - Due: Feb 11<sup>th</sup>
- Part 3 - Final Product - Due: Feb 25<sup>th</sup>
- Part 4 - Project Presentations - Feb 25<sup>th</sup> - 27<sup>th</sup>

## Overview

You will be implementing a "shell". We use a shell quite often and should have a grasp on expected shell behavior. Below is a brief overview of top level shell behavior:
- After start-up, your program should repeatedly perform these actions:
    - Print to stdout a prompt consisting of a percent sign followed by a space.
    - Read a line from stdin.
    - Lexically analyze the line and create an array of command parts (tokens). 
    - Syntactically analyze (i.e. parse) the token array to form a command.
    - Once identified, the proper command is executed:
        - It creates a child process by duplicating itself.
        - The overloaded process receives all the remaining strings given from a keyboard input (if necessary), and starts a command execution.

### Requirements

- You must use threads and execute each command in a thread.
- You should wait for the thread to complete, before returning control to the main process (unless specified to run in background).
- Your language of implementation will be decided in class (after a discussion).
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

OR

```cpp
#include <iostream>

int main(){
    std::system("ls -l");
    return 0;
}
```

The above implementations of the `ls` command with the `-l` flag, are NOT an implementation. It is a "system" call to the existing shell. I also do not expect your python implementation of the `ls` command to be as extensive as this: http://www.pixelbeat.org/talks/python/ls.py.html . Your implementations should be somewhere in between. 


### Commands To Implement

| Command   | Flag / Param                 | Meaning                                                                    |
| --------- | ---------------------------- | -------------------------------------------------------------------------- |
| `cat`     | `file`                       | concatenates a file(s) and displays results to std out                     |
|           | `file1`,`file2`,`fileN`      | display each of the files as if they were concatenated                     |
| `cd`      | `directory`                  | change to named directory                                                  |
| `cd`      |                              | change to home-directory                                                   |
|           | `~`                          | change to home-directory                                                   |
|           | `..`                         | change to parent directory                                                 |
| `chmod`   |                              | change file modes or Access Control Lists                                  |
| `cp `     | `file1 file2`                | copy file1 and call it file2                                               |
| `grep`    | `'keyword' file`             | search a file(s) files for keywords and print lines where pattern is found |
|           | `-l`                         | only return file names where the word or pattern is found                  |
| `head`    | `file`                       | display the first few lines of a file                                      |
|           | `-n`                         | how many lines to display                                                  |
| `history` |                              | show a history of all your commands                                        |
| `less`    | `file`                       | display a file a page at a time                                            |
| `ls`      |                              | list files and directories                                                 |
|           | `-a`                         | list all show hidden files                                                 |
|           | `-l`                         | long listing                                                               |
|           | `-h`                         | human readable sizes                                                       |
| `mkdir`   | `directory`                  | create a directory                                                         |
| `mv`      | `file1 file2`                | move or rename file1 to file2                                              |
| `pwd`     |                              | display the path of the current directory                                  |
| `rm`      | `file`                       | remove a file                                                              |
|           | `-r`                         | recurses into non-empty folder to delete all                               |
|           | `fil*e` or `*file` or `file* | removes files that match a wildcard                                        |
| `split`   |                              | split a file into pieces                                                   |
|           | `-b`                         | Create smaller files byte_count bytes in length                            |
|           | `-l`                         | Create smaller files n lines in length                                     |
| `sort`    |                              | sort or merge records (lines) of text (and binary) files                   |
| `tail`    | `file`                       | display the last few lines of a file                                       |
|           | `-n`                         | how many lines to display                                                  |
| `touch`   |                              | change file access and modification times                                  |
|           | `-m`                         | change the modification time of the file                                   |
|           | `-a`                         | change the access time of the file.                                        |
| `wc`      | `file`                       | count number of lines/words/characters in file                             |
|           | `-l`                         | count number of lines in file                                              |
|           | `-m`                         | count number of characters in file                                         |
|           | `-w`                         | count number of words in file                                              |
| `!x`      |                              | this loads command `x` from your history so you can run it again           |
| `who`     |                              | list users currently logged in                                             |

| Command                   | Meaning                                              |
| ------------------------- | ---------------------------------------------------- |
| `command > file`          | redirect standard output to a file                   |
| `command >> file`         | append standard output to a file                     |
| `command < file`          | redirect standard input from a file                  |
| `command1 | 2command1`    | pipe the output of command1 to the input of command2 |
| `cat file1 file2 > file0` | concatenate file1 and file2 and output to file0      |


>Note: Every command should print out help for the command if the user enters `command --help`. Look at [docstrings](https://realpython.com/documenting-python-code/) as one possible solution.

## Deliverables

#### General

- Ultimately your shell will go in your Assignments folder on github in a folder called `P01-Shell`.
- Each group member will have a copy of the project on their repo.
- The README.md file at the top level of your repository will have ALL pertinent information about your project: [Example README.md](./ExampleReadme.md).
- This readme will grow as the project grows.
- At a minimum the readme will contain lists and tables of:
  - group members with links to thier repositories
  - files with descriptions and links to each individual file
  - table of commands that were implemented and links to the documentation for the command

#### Repo
- Create a private repository on github.
- Invite rugbyprof to be a collaborator.
- Your readme will go in the repo.
- Even though your shell will have its own private repo, each member must (by the final due date) have a copy in thier assignments folder on thier own course repo.


#### Source Code

- Should be organized into seperate files.
- Every command should be in its own file.
- Each file should have a comment at the top which will be used as part of the projects "help" feature. Python has ways of pulling comments in for help if you organize your project into modules correctly.
- Links to each file will end up in your README.md.
- I cannot stress enough how amazing your readme should be. It's how I will grade your projects, aside from presentation day. 






