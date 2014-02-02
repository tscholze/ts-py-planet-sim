# -*- coding: utf-8 -*-
'''
Created on 11.12.2010

@author: falk
'''

from multiprocessing import cpu_count, Process  
from ManagedQueue import TaskManager
import sys
sys.path.append("../")
import MovePlanet as mp       #diesen Fehler in eclipse ignorieren, solange die Datei nicht verschoben wird ist der Pfad gueltig

class PlanetWorker(Process):
    
    def __calcNewPlanet(self, cs):
        return mp.calcNewPosForPlanet(cs[0], cs[1], cs[2], cs[3])
    
    def __workerFunction(self, jobQueue, resultQueue):
        while True:
            task = jobQueue.get()
            result = self.__calcNewPlanet(task)
            resultQueue.put(result)
            jobQueue.task_done()
    
    def __startWorkers(self, m):
        jobQueue, resultQueue = m.getJobQueue(), m.getResultQueue()
        nrOfProcesses = cpu_count()
        for i in range(nrOfProcesses):
            p = Process(target = self.__workerFunction,
                    args = (jobQueue, resultQueue))
            p.start()
    def run(self):
        sIp = 'localhost'
        #sIp = '192.168.178.39'
        #sIp = 'hercules.informatik.fh-augsburg.de'
        sSocket = 10019
        TaskManager.register('getJobQueue')
        TaskManager.register('getResultQueue')
        m = TaskManager(address=(sIp, sSocket), authkey = 'secret')
        m.connect()
        self.__startWorkers(m)