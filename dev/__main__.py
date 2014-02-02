# -*- coding: utf-8 -*-
'''
Created on Dec 18, 2010

@author: falk
'''

from planetSim import PlanetSimulation
import sys
from PyQt4 import QtGui
from multiprocessing import Process
from distributed_computing.ManagedQueue import TaskManager

if __name__ == '__main__':
    
    tm = TaskManager()
    tmP = Process(target=tm.selfConfig)
    tmP.start()
    
    app = QtGui.QApplication(sys.argv)
    uiDemo = PlanetSimulation()
    
    sys.exit(app.exec_())
    
    tmP.terminate()
    
    