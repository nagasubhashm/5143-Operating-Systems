from math import pow
import sys
import os
from random import shuffle
from random import randint

# Help to format a binary string 
# important: "width" = bits in address space
binformat = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=12, type='b')

def read_file(fin,delimiter="\n"):
    if os.path.isfile(fin):
        with open(fin) as f:
            data = f.read()
        data = data.strip()
        return data.split(delimiter)
    print("Error: file does not exist in function 'read_file'...")
    return None

def str_binary(n,bits=12):
    frmt = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=bits, type='b')
    return format(n,frmt)

# Address allocation within address space
# stack
# empty
# heap
# data
# code

processes = 3

virt_mem_size = 4096 # bytes
#virt_mem_size = 256 # bytes
phys_mem_size = 128
page_size = 8 # bytes

process_list = [x for x in range(processes)]
memory_access = []

for x in range(500):
    memory_access.append(randint((virt_mem_size-1024),virt_mem_size))

f = open("prog_1.dat","w")

for i in range(100):
    shuffle(memory_access)
    shuffle(process_list)
    f.write("{},{} ".format(process_list[0],hex(memory_access[0])[2:]))

f.close()

data = read_file("prog_1.dat"," ")

for d in data:
    p,h = d.split(',')
    n = int(h, 16)
    b = str_binary(n,5)
    
    print("{} {} {} {}".format(p,h,n,b))
