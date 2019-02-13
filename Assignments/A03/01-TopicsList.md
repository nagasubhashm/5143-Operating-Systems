### Multi-Multi-Multi
  - Multiprogramming
    - define
    - Is number of processors significant and or supported?
    - historical significance
    - timeline
    - context switching (in this context) :)
  - Multiprocessing
    - define
    - Is number of processors significant and or supported?
    - historical significance
    - timeline
    - categories
      - massively parallel processing
      - symmetric multiprocessing
  - Multitasking
    - define
    - Is number of processors significant and or supported?
    - historical significance
    - timeline
  - Multithreading
    - define
    - Is number of processors significant and or supported?
    - historical significance
    - timeline
    - context switching (in this context) :)


### Concurrency: Mutual Exclusion and Synchronization
- Principles of Concurrency
- Mutual Exclusion: Hardware Support
- Semaphores 
- Monitors 
- Message Passing 
- Readers/Writers Problem 

|                  |     Key Words      |                      |
|:----------------:|:------------------:|:--------------------:|
|      atomic      |  binary semaphore  |       blocking       |
|   busy waiting   |    concurrency     | concurrent processes |
|    coroutine     | counting semaphore |  critical resource   |
| critical section |      deadlock      |  general semaphore   |
| message passing  |      monitor       |   mutual exclusion   |
|      mutex       |    nonblocking     |    race condition    |
|    semaphore     |    spin waiting    |      starvation      |
| strong semaphore |   weak semaphore   |                      |

### Concurrency: Deadlock and Starvation

- Principles of Deadlock
- Deadlock Prevention
- Deadlock Avoidance
- Deadlock Detection
- An Integrated Deadlock Strategy
- Dining Philosophers Problem

|                     |     Key Words      |                           |
|:-------------------:|:------------------:|:-------------------------:|
| banker’s algorithm  |   circular wait    |    consumable resource    |
|      deadlock       | deadlock avoidance |    deadlock detection     |
| deadlock prevention |   hold and wait    |  joint progress diagram   |
|   memory barrier    |      message       |     mutual exclusion      |
|        pipe         |     preemption     | resource allocation graph |
|  reusable resource  |      spinlock      |        starvation         |

### Memory Management
- Job Queue
- Binding Instructions to Memory
- Logical vs Physical Address Space
- MMU (Memory Management Unit)
- Dynamic Relocation
- Swapping
- Paging
  - Dirty Bit
  - Page Fault
- Memory Allocation
  - Contiguous
- Fragmentation
    - External
    - Internal
- Paging
- Segmentation

### Scheduling Algorithms

- **First Come First Serve (FCFS)**: Simplest scheduling algorithm that schedules according to arrival times of processes.

- **Shortest Job First(SJF)**: Process which have the shortest burst time are scheduled first.

- **Longest Job First(LJF)**: It is similar to SJF scheduling algorithm. But, in this scheduling algorithm, we give priority to the process having the longest burst time. This is non-preemptive in nature i.e.,when any process starts executing, can’t be interrupted before complete execution.

- **Shortest Remaining Time First(SRTF)**: It is preemptive mode of SJF algorithm in which jobs are schedule according to shortest remaining time.

- **Longest Remaining Time First(LRTF)**: It is preemptive mode of LJF algorithm in which we give priority to the process having largest burst time remaining.

- **Round Robin Scheduling**: Each process is assigned a fixed time in cyclic way.

- **Priority Based scheduling (Non Preemptive)**: In this scheduling, processes are scheduled according to their priorities, i.e., highest priority process is schedule first. If priorities of two processes match, then schedule according to arrival time.

- **Highest Response Ratio Next (HRRN)**: In this scheduling, processes with highest response ratio is scheduled. This algorithm avoids starvation.

- **Multilevel Queue Scheduling**: According to the priority of process, processes are placed in the different queues. Generally high priority process are placed in the top level queue. Only after completion of processes from top level queue, lower level queued processes are scheduled.

- **Multi level Feedback Queue Scheduling**: It allows the process to move in between queues. The idea is to separate processes according to the characteristics of their CPU bursts. If a process uses too much CPU time, it is moved to a lower-priority queue.
  
### I/O & Disk Scheduling
  
### File Management
