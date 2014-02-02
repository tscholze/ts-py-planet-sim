'''
Created on Dec 18, 2010

@author: falk
'''

import multiprocessing
from ObjectGenerator import ObjectGenerator
from Printer import Printer

if __name__ == '__main__':
    i = 0
    end1, end2 = multiprocessing.Pipe()
    p = Printer(end1, i)
    og = ObjectGenerator(end2, i)
    
    #proc2 = multiprocessing.Process(target=og.run(), args=('',))
    #proc1 = multiprocessing.Process(target=p.run(), args=('',))
    #print "processes created"
    p.start()
    #print "process 2 started"
    og.start()
    #print "process 1 started"