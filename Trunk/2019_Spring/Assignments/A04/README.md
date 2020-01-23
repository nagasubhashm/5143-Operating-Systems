## Virtual Memory - Simulation / Analysis
#### Due: 24 Apr 

### Overview

<img src='http://cs.mwsu.edu/~griffin/zcloud/zcloud-files/vm_multiple_processes.png' width=500>

- In this assignment you will test the efficacy of various virtual memory paging schemes.  You will implement four different paging schemes: 
  - First-In-First-Out
  - Least Recently Used 
  - Least Frequently Used
  - Random Replacement
  - Optimal Replacement (tentative)

----

- **First-In-First-Out (FIFO) Replacement**
    - On a page fault, the frame that has been in memory the longest is replaced.
-  **Least Recently Used (LRU) Replacement**
    - On a page fault, the frame that was least recently used in replaced.
- **Least Frequently Used (LFU) Replacement**
    - This is a little more involved. We need to keep track of:
      - <i><b>S<sub>t</sub></b></i> = Sum of ***all*** page accesses ***since*** time <i><b>t</b></i>.
      - <i><b>s<sub>i</sub></b></i> = Sum of page accesses for page <i><b>i</b></i>.
      - <i><b>f<sub>i</sub></b></i> = <i><b>s<sub>i</sub></b></i> / <i><b>S<sub>t</sub></b></i>
- **Optimal Replacement**
    - The Optimal algorithm cheats. It looks forward in time to see which frame to replace on a page fault. Thus it is not a real replacement algorithm. It gives us a frame of reference for a given static frame access sequence.
- **Random Replacement**
    - On a page fault, choose a frame at random and replace it.
----

### Components

You will write a python program that will simulate a page table for for each process. There will obviously be a lot of abstraction in our implementation, mainly we will be using strings as addresses and parsing strings to obtain page numbers ~~and offsets~~. Since we are not actually executing instructions, using bits as an offset into the page is not necessary for this simulation.

The main component will be the page table itself. You can use whatever data structure you like, however I would recommend a setup similar to the following:

```python

class page_frame(object):
    def __init__():
        self.valid_bit = False  # in memory
        self.dirty = False      # updated
        self.last_access = 0    # time stamp
        self.access_count = 0   # sum of accesses



class page_table(object):
    def __init__(virt_mem_page_count,phys_mem_size):
        self.vm_page_count = virt_mem_page_count
        self.pm_size = phys_mem_size

        self.page_table = {}        # dictionary of page_frames

class physical_memory(object):
    def __init__(mem_size):
        self.mem_size = mem_size

        self.mem_table = {}        # dictionary of page_frames
```

### Processes / Instructions

A process in the case of our simulation will be a space delimited file of randomly generated hex addresses. These hex addresses will be considered `page numbers`. So, there are no real "instructions" (e.g. `add R3 , R2, R0` or `ld R1 1024(R7)`), only page accesses. Each `process_id` will be accompanied with a `hex address` that represents a page access. An example input file could look like:

```
1,0x6d 1,0x8 1,0x12 1,0x22 1,0x10 1,0xf 1,0x72 1,0x2 2,0x9 1,0x78 1,0xa 1,0x6d 1,0x7 0,0xf 0,0x73 2,0x1 0,0x5 1,0xd 1,0x5 1,0x22 1,0x26 1,0x69 1,0x7 1,0xf 1,0x1d 1,0x79 1,0x4 1,0x16 1,0x22 1,0x7a 0,0xa 1,0x7a 1,0x5 2,0x72 0,0x21 1,0x17 1,0x16 1,0x17 2,0x7c 2,0x72 1,0x9 0,0x18 1,0x1e 1,0x5 1,0x7a 1,0x71 1,0x19 1,0x20 1,0x66 1,0x75 1,0x24 1,0x10 1,0x1f 1,0x77 0,0x11 1,0x69 1,0x15 0,0x74 1,0x6b 1,0xe 1,0xb 0,0x7e 0,0x73 1,0x74 1,0x74 0,0x18 2,0x25 1,0x1a 1,0xa 1,0xa 2,0x17 1,0x78 1,0x20 1,0x7 1,0xd 2,0x6b 0,0x67 1,0x15 1,0x7b 2,0xc 1,0x3 1,0x6e 1,0x7f 1,0x24 2,0x69 0,0x1b 1,0x5 1,0x23 1,0x1f 0,0x12 2,0x14 1,0x16 1,0x7c 1,0x7d 1,0x26 1,0x13 1,0x4 1,0x74 0,0x69 1,0x8 1,0x25 1,0x1c 1,0x1d 0,0x14 1,0x6 1,0x15 1,0x5 1,0x1c 1,0x7f 1,0x6c 1,0x4 0,0x17 1,0x6 0,0x6 1,0xa 1,0xe 1,0x76 0,0x14 1,0x70 0,0x80 2,0x74 2,0xa 0,0x71 0,0x70 0,0x19 0,0xd 0,0x4 1,0x15 1,0x1f 1,0x20 1,0x1e 0,0x6c
```

- Input files can be obtained from: `http://cs.mwsu.edu/~griffin/vm_snapshots/` 

### Running your Program

Your program should be configurable from the command line giving a directory of files to process. For example:

```sh
python virtual.py directory=./snapshots
or 
python virtual.py data_file=input_files.txt
```
- If you use the `directory` option, the provided `directory name` should have all the files you plan to run in your simulation
- If you use the `data file` option, the file should contain a json list of filenames to `get` from the cs server.
- However you do it is fine.

Each file in the directory will be named using a specific convention. You can process each file name like so:


#### Processing File Name
```python
p = './snapshots/sim_11_50_1024_512.dat'            # path to file
f = os.path.basename(p)                             # get basename (remove path)
name, ext = f.split('.')                            # split name from extension
s,run,np,vm,pm = split('sim_11_50_1024_512').('_')  # get each piece of info
```

#### Gives US
```python
s = sim     # ignore
run = 11    # ignore
np = 50     # number of processes
vm = 1024   # virt mem size
pm = 512    # phys mem size
```

Basically, each filename is used to configure your simulation for a specific run. The only item not given is `page size`. But since we are not using `page size` to configure anything, we don't need it.

Again, a file contains: 
```
1,0x6d 0,0x8 0,0x12 1,0x22 2,0x10 1,0xf 1,0x72 0,0x2 2,0x9 1,0x78 1,0xa 1,0x6d 2,0x7 0,0xf 0,0x73 ...
```

And we would process this like:

```
1,0x6d  = Process 1 accesses line 109
0,0x8   = Process 0 accesses line 008
0,0x12  = Process 0 accesses line 018
1,0x22  = Process 1 accesses line 034
2,0x10  = Process 2 accesses line 016
1,0xf   = Process 1 accesses line 015
1,0x72  = Process 1 accesses line 114
1,0x6d  = Process 1 accesses line 109
2,0x6d  = Process 2 accesses line 109
```

Using these data accesses you should:
  - Check to see if "line x" is in virtual memory
    - If it is:
      - Check to see if it is valid (still in physical memory)
    - If it is not:
      - Execute a page fault and replace physical memory page using your current replacement algorithm.

What are you counting?
- Keep a tally of page faults for each:
  - replacement algorithm
  - process number
  - vm size
  - pm size

### Page Fault

- A page fault is when the CPU requests an address and its mapping shows it not to be in main memory. In other words, we need to access disk, replace a page in memory with the newly accessed page. 
- Do we need to write the old page back to disk? Only if any portion of the page was changed (dirty bit), but we are not looking to write back changes in this simulation.

#### Purpose of Simulation

- We are simply counting page faults to compare each of the replacement algorithms.

### Deliverables

- Create a folder called `A04` in your assignments folder.
- Write a `driver.py` that will read in every file in a folder called `vm_snapshots`.
- The naming convention of each file will determine the virtual memory size and number of processes.
- Your code will loop through a predefined set of page sizes (to be discussed in class).
- You will provide a plot diagram for each "run" that you perform (to be discussed in class).
- All code used should be in your assignment folder.
- All diagrams created should be in your assignment folder.


#### Helpful Snippets

- [read.py](./read.py)

- Usefull function to grab key value pairs off of command line:
>NOTE: Must be `key=val` with no spaces! 
```python
def kvargs(sysargs):
    args = {}

    # traverse copy of sys.argv skipping first element
    for val in sysargs[1:]:
        k,v = val.split('=')
        args[k] = v
    return args
```

- Python has a library called `Requests`: http://docs.python-requests.org/en/master/user/quickstart/

```python
import requests

r = requests.get('http://cs.mwsu.edu/~griffin/vm_snapshots/sim_0_3_128.dat')

data = r.text.split(' ')

for item in data:
    p,add = item.split(',')
    
    print("p:{} , add:{}".format(p,add))
```
