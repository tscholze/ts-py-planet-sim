# -*- coding: utf-8 -*-
'''
Created on 11.12.2010

@author: falk
'''
from multiprocessing.managers import BaseManager # managedQueue.py
from multiprocessing import JoinableQueue, Queue

class TaskManager(BaseManager):
    
    __adr = ('', 10019)
    __authkey = 'secret'
    
    def selfConfig(self):
        taskQueue = JoinableQueue()
        resultQueue = Queue()
        TaskManager.register('getJobQueue', 
                             callable = lambda:taskQueue)
        TaskManager.register('getResultQueue', 
                             callable = lambda:resultQueue)
        m = TaskManager(self.__adr, self.__authkey)
        m.get_server().serve_forever()