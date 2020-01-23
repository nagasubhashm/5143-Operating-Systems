# https://stackoverflow.com/questions/28267972/python-multiprocessing-locks
# https://hackernoon.com/synchronization-primitives-in-python-564f89fee732

import multiprocessing
import time

l = multiprocessing.Lock()

def job(num):
  l.acquire()
  print num
  l.release()
  time.sleep(1)

pool = multiprocessing.Pool(4)

lst = range(40)
for i in lst:
  pool.apply_async(job, [i])

pool.close()
pool.join()