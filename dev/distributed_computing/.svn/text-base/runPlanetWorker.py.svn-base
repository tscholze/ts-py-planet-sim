'''
Created on Dec 19, 2010

@author: falk
'''

from PlanetWorker import PlanetWorker
import multiprocessing

if __name__ == '__main__':
    listOfWorker = list()
    numberOfWorker = multiprocessing.cpu_count()
    
    for i in range(numberOfWorker):
        newWorker = PlanetWorker()
        listOfWorker.append(newWorker)
        newWorker.start()