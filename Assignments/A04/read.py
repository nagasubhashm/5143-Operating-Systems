import sys
import os

def str_binary(n,padd=12):
    binfrmt = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=padd, type='b')
    n = format(n,binfrmt)
    return n

def usage(e):
    print("do it right...")
    print(e)
    sys.exit()

def myargs(sysargs):
    args = {}

    for val in sysargs[1:]:
        k,v = val.split('=')
        args[k] = v
    return args

def read_file(fin,delimiter="\n"):
    if os.path.isfile(fin):
        with open(fin) as f:
            data = f.read()
        data = data.strip()
        return data.split(delimiter)
    usage("Error: file does not exist in function 'read_file'...")
    return None

if __name__=='__main__':

    args = myargs(sys.argv)

    if not 'filename' in args:
        usage("Error: filename not on command line...")

    data = read_file(args['filename']," ")

    for d in data:
        p,h = d.split(',')
        n = int(h, 16)
        b = str_binary(n,7)

        print("{} {} \t{} \t{}".format(p,h,n,b))