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

The main component will be the page table itself. You can use whatever data structure you like, however I would recommend a similar setup to the following:

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

Each `hex address` will be accompanied with a `process_id`. An example input file could look like:





### Running your Program

Your program should be configurable from the command line giving sizes for each component in bytes. For example:

```sh
python virtual.py vm=2048 pm=64 ps=8 n=15
```

Where:
- vm = 2k of virtual memory
- pm = 64 bytes of physical memory
- ps = 8 byte page size
- n = number of processes