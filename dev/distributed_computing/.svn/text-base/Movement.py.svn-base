# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 08:50:30 2010

@author: falk
"""
from __future__ import division

class Movement(object):
    
    def __init__(self, master):
        self.__master = master
        
    def updateSunsystem(self, sunsystem, timePerStep = 1, MaxDistancePerStep = 1e9):
        for planet in sunsystem:
            self.__master.putJob((planet, sunsystem, timePerStep, MaxDistancePerStep))
        newSunsystem = list()
        while len(newSunsystem) < len(sunsystem):
            result = self.__master.getResult()
            if result is not None:
                newSunsystem.append(result)
        #sort the new sunsystem that it fits to the actors in the gui
        newSunsystem = sorted(newSunsystem, key = lambda planet: planet.id)
        return newSunsystem