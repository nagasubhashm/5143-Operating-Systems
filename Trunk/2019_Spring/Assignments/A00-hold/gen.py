from math import pow
from math import log2
import sys
import os
from random import seed 
from random import shuffle
from random import randint
import binascii


def str_binary(n,padd=12):
    binfrmt = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=padd, type='b')
    n = format(n,binfrmt)
    return n

def rand_binary_address(max_size=4096):
    """
    """
    bits = int(log2(vm_size))
    hbase = int(vm_size*.8)
    lbase = int(vm_size*.3)
    highlow_chances = [1,1,1,0,0,0,0,0,0,0]

    shuffle(highlow_chances)
    highlow = highlow_chances[0]

    address = 0

    if highlow > 0:
        address = randint(hbase,max_size-1)
    else:
        address = randint(0,lbase)

    return str_binary(address,bits)

def rand_instruction(symbol=None):
    """
    Create a random instruction. 
    Example:
        add xxx 89  
        would add 89 to value contained in symbol xxx and store result in xxx
    Param:
        symbol [string,None]: name of symbol 
    Returns:
        string : random symbol
    """
    
    itype = ['add','sub','mul','div'] #instruction type

    shuffle(itype)

    if symbol == None:
        symbol = gen_rand_symbol()

    instruction = "{} {} {}".format(itype[0],str(symbol),randint(1,100))
    
    return instruction



def gen_instructions(minimum_instructions,max_instructions,symbol_table):
    """
    Generate random instructions

    Params:
        minimum_instructions [int]: min number of instructions
        max_instructions [int]: max number
        symbol_table [dictionary]: dictionary of symbols
    Returns:
        list: list of instructions
    """
    process_instructions = []

    num_inst = randint(minimum_instructions,max_instructions)
    #sys.stdout.write("\t\t"+str(num_inst)+"\n")
    for x in range(num_inst):
        i = randint(0,len(symbol_table)-1)
        symbols = list(symbol_table.keys())
        process_instructions.append(rand_instruction(symbols[i]))

    shuffle(process_instructions)
    return process_instructions

def gen_rand_symbol(size=3):
    """
    Generate a random symbol

    Params:
        size [int]: size of symbol
    Returns:
        string: symbol
    """
    letters = [chr(i) for i in range(65,91)]
    #letters.extend([chr(i) for i in range(97,122)])

    symbol = ''

    for i in range(size):
        shuffle(letters)
        symbol = symbol + letters[i]

    return symbol

def gen_symbol_table(min_size=1,max_size=50):
    """
    Generate a symbol table 

    Params: 
        min_size [int]: minimum symbols 
        max_size [int]: max number of symbols

    Returns:
       dict: dictionary of symbols initialized to zero
    """
    table = {}

    i = randint(min_size,max_size)

    
    while i > 0:
        symbol = gen_rand_symbol(randint(3,3))
        if not symbol in table:
            table[symbol] = 0
            i -= 1
    return table

def write_process_file(process_instructions,pid):
    """
    write randomly generated instructions to a file

    Params:
        process_instructions [list]: list of instructions
        pid [int]: process id
    Returns:
        bool: success or fail
    """
    name = "process_{}.dat".format(pid)

    f = open(os.path.join('processes',name),"w")

    for p in process_instructions:
        h = "{}".format(p.encode().hex())
        print(len(h))
        h = h.zfill(32)
        f.write(h)

    f.close()

    return os.path.isfile(os.path.join('processes',name))

def read_process_file(path):
    pos = 0
    f = open(path,"r")
    f.seek(pos)
    
    for chunk in iter(lambda: f.read(32), ''):
        inst = bytearray.fromhex(chunk).decode()
        print(inst)


if __name__=='__main__':

    seed(345678)

    minimum_instructions = 512
    max_instructions = int(pow(2,17))

    t = gen_symbol_table(randint(10,100))
    instructions = gen_instructions(minimum_instructions,max_instructions,t)
    write_process_file(instructions,'1')
    read_process_file('./processes/process_1.dat')

    