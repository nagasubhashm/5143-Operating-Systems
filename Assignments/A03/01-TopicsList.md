### Multi-Multi-Multi (Tanaka and Mika Feb 25th)
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

### Concurrency: Deadlock and Starvation (Mika)  Feb 27<sup>th</sup>

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


### Concurrency: Mutual Exclusion and Synchronization (Tanaka Ndem Sun) March 4th
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



### Memory Management (Daniel) March 11-13
- Job Queue(Daniel)
- Binding Instructions to Memory
- Logical vs Physical Address Space
- MMU (Memory Management Unit)
- Dynamic Relocation
- Swapping
- Paging (Daniel)
  - Dirty Bit(Daniel)
  - Page Fault(Daniel)
- Memory Allocation(Daniel)
  - Contiguous(Daniel)
- Fragmentation(Daniel)
    - External(Daniel)
    - Internal(Daniel)
- Paging(Daniel)
- Segmentation(Daniel)

### Scheduling Algorithms March 25-27

- **First Come First Serve (FCFS)**: Simplest scheduling algorithm that schedules according to arrival times of processes. (Ben and Garrett)

- **Shortest Job First(SJF)**: Process which have the shortest burst time are scheduled first. (Ben and Garrett)

- **Longest Job First(LJF)**: It is similar to SJF scheduling algorithm. But, in this scheduling algorithm, we give priority to the process having the longest burst time. This is non-preemptive in nature i.e.,when any process starts executing, can’t be interrupted before complete execution. (Ben and Garrett)

- **Shortest Remaining Time First(SRTF)**: It is preemptive mode of SJF algorithm in which jobs are schedule according to shortest remaining time. (Ben and Garrett)

- **Longest Remaining Time First(LRTF)**: It is preemptive mode of LJF algorithm in which we give priority to the process having largest burst time remaining.(Ben and Garrett)

- **Round Robin Scheduling**: Each process is assigned a fixed time in cyclic way.(Ben and Garrett)

- **Priority Based scheduling (Non Preemptive)**: In this scheduling, processes are scheduled according to their priorities, i.e., highest priority process is schedule first. If priorities of two processes match, then schedule according to arrival time.[sairamkrishna and saikiran]

- **Highest Response Ratio Next (HRRN)**: In this scheduling, processes with highest response ratio is scheduled. This algorithm avoids starvation.[sairamkrishna and saikiran]

- **Multilevel Queue Scheduling**: According to the priority of process, processes are placed in the different queues. Generally high priority process are placed in the top level queue. Only after completion of processes from top level queue, lower level queued processes are scheduled.[sairamkrishna and saikiran]

- **Multi level Feedback Queue Scheduling**: It allows the process to move in between queues. The idea is to separate processes according to the characteristics of their CPU bursts. If a process uses too much CPU time, it is moved to a lower-priority queue.[sairamkrishna and saikiran]
  
### I/O & Disk Scheduling (Sai Nagesh and Havila) April 4-6

https://intro2operatingsystems.wordpress.com/2016/05/11/mass-storage-and-disk-scheduling/
  
### File Management
