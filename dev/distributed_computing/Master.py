# -*- coding: utf-8 -*-
'''
Created on 11.12.2010

@author: falk
'''
from ManagedQueue import TaskManager

class Master(object):
    sIp = 'localhost'
    sSocket = 10019
    authkey = 'secret'
    
    def __init__(self):
        TaskManager.register('getJobQueue')
        TaskManager.register('getResultQueue')
        m = TaskManager((self.sIp, self.sSocket), self.authkey)
        m.connect()
        self.__jobQueue, self.__resultQueue = m.getJobQueue(), m.getResultQueue()
        
    def putJob(self, job):
        self.__jobQueue.put(job)
        
    def getResult(self):
        #self.__jobQueue.join()
        return self.__resultQueue.get()