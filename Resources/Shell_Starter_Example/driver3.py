#!/usr/bin/env python
from cmd_pkg import commands 
import threading
import sys


class Shell(object):
    def __init__(self,**kwargs):
        if 'cmd' in kwargs:
            self.cmd = kwargs['cmd']
        if 'size' in kwargs:
            self.cmd = kwargs['size']
        if 'memory' in kwargs:
            self.cmd = kwargs['memory']
        if 'cache' in kwargs:
            self.cache = kwargs['cache']

        print(self)

    def showArgs(self,first,*args):
        print(first)
        for arg in args:
            print(arg)

    def showkArgs(self,first,**kwargs):
        print(first)
        for k,v in kwargs.items():
            print(k)
            print(v)

    def run_command(self,cmd,args=None,flags=None):

        if args:
            c = threading.Thread(target=cmd, args=args)
        else:
            c = threading.Thread(target=cmd)
            
        c.start()
        c.join()

    def shellLoop(self):
        while True:
            cmd = raw_input('% ')
            cmd = cmd.split()
            
            if cmd[0] == 'cat':
                cat(cmd[1])
                print()
            elif cmd[0] == 'grep':
                if(len(cmd) < 3):
                    run_command(commands.grepusage)
                else:
                    run_command(commands.grep,(cmd[1],cmd[2],))

            if cmd[0] == 'exit':
                break
            

if __name__=='__main__':
    S = Shell(cmd='grep',size=8,memory=['godzilla','kraken'])
    #S.shellLoop()
    #S.showkArgs('i am first',)
    print(dir(S))

        