## Virtual Memory - Simulation / Analysis
#### Due: TBD

In this assignment you will test the efficacy of various virtual memory paging schemes.  You will implement four different paging schemes: first-in-first-out, least-recently used, least-frequently used (using a definition specified below), and optimal.

### Schemes

- **First-In-First-Out (FIFO) Replacement**
    - On a page fault, the frame that has been in memory the longest is replaced.
-  **Least Recently Used (LRU) Replacement**
    - On a page fault, the frame that was least recently used in replaced.
- **Least Frequently Used (LFU) Replacement**
    - This is a little more involved. We need to keep track of:
      - `S` = Sum of ***all*** page accesses ***since*** this page-frame was loaded
      - <i>s</i><sub>i</sub> = Sum of page accesses for 