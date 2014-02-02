# -*- coding: utf-8 -*-
'''
Created on 11.12.2010

@author: falk

1. managedQueue
2. CreateServer
3. worker
4. moreWorker
'''

from PlanetSim.dev.distributed_computing.Movement import Movement

if __name__ == '__main__':
    m = Movement()
    
    for i in range(100):
        m.putJob(i)
    
    while True:
        r = m.getResult()
        if r is not None:
            print r