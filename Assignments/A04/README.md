## Virtual Memory - Simulation / Analysis
#### Due: TBD

### Overview

- In this assignment you will test the efficacy of various virtual memory paging schemes.  You will implement four different paging schemes: 
  - First-In-First-Out
  - Least Recently Used 
  - Least Frequently Used
  - Optimal Replacement

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

----

### Components

You will write a python program that will simulate a page table for virtual memory. There will obviously be a lot of abstraction in our implementation, mainly we will be using strings as addresses and parsing strings to obtain page numbers and offsets.

The main component will be the page table itself. You can use whatever data structure you like, however I would recommend asetup similar to the following:

```python

class page_frame(object):
    def __init__():
        self.valid_bit = False
        self.dirty = False
        self.last_access = 0
        self.access_count = 0



class page_table(object):
    def __init__(virt_mem_size=4096,phys_mem_size=128,page_size=8):
        self.vm_size = virt_mem_size
        self.pm_size = phys_mem_size
        self.page_size = page_size

        self.page_table = {}    # dictionary of page_frames
    
```

### Processes / Instructions

A process in the case of our simulation will be a space delimited file of randomly generated hex addresses. These hex addresses will be considered `memory accesses`. So, there are no real "instructions" (e.g. `add R3 , R2, R0` or `ld R1 1024(R7)`). There are simply simulated memory accesses. 

Each `process_id` will be accompanied with a `hex address`. An example input file could look like:

```
1,0x6d 1,0x8 1,0x12 1,0x22 1,0x10 1,0xf 1,0x72 1,0x2 2,0x9 1,0x78 1,0xa 1,0x6d 1,0x7 0,0xf 0,0x73 2,0x1 0,0x5 1,0xd 1,0x5 1,0x22 1,0x26 1,0x69 1,0x7 1,0xf 1,0x1d 1,0x79 1,0x4 1,0x16 1,0x22 1,0x7a 0,0xa 1,0x7a 1,0x5 2,0x72 0,0x21 1,0x17 1,0x16 1,0x17 2,0x7c 2,0x72 1,0x9 0,0x18 1,0x1e 1,0x5 1,0x7a 1,0x71 1,0x19 1,0x20 1,0x66 1,0x75 1,0x24 1,0x10 1,0x1f 1,0x77 0,0x11 1,0x69 1,0x15 0,0x74 1,0x6b 1,0xe 1,0xb 0,0x7e 0,0x73 1,0x74 1,0x74 0,0x18 2,0x25 1,0x1a 1,0xa 1,0xa 2,0x17 1,0x78 1,0x20 1,0x7 1,0xd 2,0x6b 0,0x67 1,0x15 1,0x7b 2,0xc 1,0x3 1,0x6e 1,0x7f 1,0x24 2,0x69 0,0x1b 1,0x5 1,0x23 1,0x1f 0,0x12 2,0x14 1,0x16 1,0x7c 1,0x7d 1,0x26 1,0x13 1,0x4 1,0x74 0,0x69 1,0x8 1,0x25 1,0x1c 1,0x1d 0,0x14 1,0x6 1,0x15 1,0x5 1,0x1c 1,0x7f 1,0x6c 1,0x4 0,0x17 1,0x6 0,0x6 1,0xa 1,0xe 1,0x76 0,0x14 1,0x70 0,0x80 2,0x74 2,0xa 0,0x71 0,0x70 0,0x19 0,0xd 0,0x4 1,0x15 1,0x1f 1,0x20 1,0x1e 0,0x6c 0,
```

- Input files can be obtained from: `http://cs.mwsu.edu/~griffin/vm_snapshots/` 
- Python has a library called `Requests`: http://docs.python-requests.org/en/master/user/quickstart/

```python
import requests

r = requests.get('http://cs.mwsu.edu/~griffin/vm_snapshots/sim_0_3_128.dat')

data = r.text.split(' ')

for item in data:
    p,add = item.split(',')
    
    print("p:{} , add:{}".format(p,add))
```

### Running your Program

Your program should be configurable from the command line giving sizes for each component in bytes. For example:

```sh
python virtual.py vm=2048 pm=1024 ps=256 n=15
```

Where this run would be configured using:
- vm = 2048 bytes of virtual memory
- pm = 1024 bytes of physical memory
- ps = 256 bytes
- n = number of processes

Usefull function to grab key value pairs off of command line:
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

### Page Fault

- A page fault is when the CPU requests an address and its mapping shows it not to be in main memory. In other words, we need to access disk, replace a page in memory with the newly accessed page. 
- Do we need to write the old page back to disk? Only if any portion of the page was changed (diry bit), but we are not looking for any changes in this simulation.

### Purpose of Simulation

- Simply, we are counting page faults using each of the scheduling algorithms.

### Deliverables

- Create a folder called `A04` in your assignments folder.
- Write a `driver.py` that will read in every file in a folder called `vm_snapshots`.
- The naming convention of each file will determine the virtual memory size and number of processes.
- Your code will loop through a predefined set of page sizes (to be discussed in class).
- You will provide a plot diagram for each "run" that you perform (to be discussed in class).
- All code used should be in your assignment folder.
- All diagrams created should be in your assignment folder.

#### Possible Runs

- Loop through each file : ['./snapshots/sim_1_5_256.dat' , ... , './snapshots/sim_35_100_4096.dat']
- Nameing convention:
  - `sim_20_50_1024`
  - `20` = `Filenumber`
  - `50` = `Number of processes`
  - `1024` = `Virtual Memory size`
- Virtual Memory (`VM`) is typically 1.5 - 4 times the size of physical memory so we should test our simulation on multiple physical memory (`PM`) sizes.
  - `VM` = 1024 
  - Possible `PM` sizes:
    - 2^9 = 512
    - 2^8 = 256
    - 2^7 = 128

More coming ... Discuss in class...