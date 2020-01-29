## Threading - Messing w/ Matrices 
#### Due: TBD

### Brief Overview

- Assume there are three `nxn` arrays => `A`, `B`, and `C`
- Randomly populate `A` and `B` with random numbers.
- Add `A` and `B` together storing result in `C`

### Using Threads

- This time the goal is to still add `A` and `B` together storing result in `C` but using `t` threads to do so. 
- Each thread will be responsible for adding a portion of `A` and `B` and storing in `C`


### Specifics

- Using `sys.argv` to pass in key value params
- Example command:
  - python matrix.py n=10000 t=10 row=5000 rval=11 col=300 cval=7
- Pass in the following params:
  - `n`: width and height of array
  - `t`: number of threads (`n` should be divisible by `t`)
  - `row`: the row in wich to assign `rval` to. Above example means apply the value `11` to the entire row `5000`.
  - `col`: same as row but for column.

### Questions

- The goal is to force the system to use virtual memory (hence the large array size) and force paging as array indexes change.
- Do number of threads speed up the result?
- 