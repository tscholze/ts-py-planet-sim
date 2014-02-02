# -*- coding: utf-8 -*-
'''
Created on 21.11.2010

@author: falk

Berechnet die Flugbahn einfacher Himmelskörper. Es werden beliebig viele fest vorgegebene Körper simuliert.
'''
import sys
sys.path.append("../")

from PlanetSim.dev.Planet import Planet
from PlanetSim.dev import MovePlanet as mp

import numpy
import pylab

if __name__ == '__main__':
    #sun = Planet(0, 9999999, 1, numpy.array([0, 0.000001, 0]), numpy.array([0, 0.00001, 0]))
    #sun =  Planet("Sonne", 2.054e30, 696e6, numpy.array([0.0,0.0,0.0]), numpy.array([0.0,0.0,0.0]))
    sun =  Planet("Sonne", 2.054e30, 696e6, numpy.array([0.0,0.0,0.0]), numpy.array([0.0,0.0,0.0]))
    
    #earth = Planet(1, 1, 1, numpy.array([100, 100, 0]), numpy.array([1, 1, 0]))
    merkur = Planet( "Merkur", 3.30e23, 244e4, numpy.array([57.91e9, 0.0,0.0]), numpy.array([0.0, 47.9e3, 0.0]))
    venus = Planet( "Venus", 4.87e24, 6052e3, numpy.array([108.94e9, 0.0,0.0]), numpy.array([0.0, 35.05e3, 0.0]))
    earth = Planet( "Erde", 5.97e24, 6371e3, numpy.array([149.6e9, 0.0,0.0]), numpy.array([0.0, 29.8e3, 0.0]))
    mars = Planet( "Mars", 6.42e23, 3390e3, numpy.array([227.94e9, 0.0,0.0]), numpy.array([0.0, 24.24e3, 0.0]))
    jupiter = Planet( "Jupiter", 1.90e27, 69911e3, numpy.array([778.57e9, 0.0,0.0]), numpy.array([0.0, 13.01e3, 0.0]))
    saturn = Planet( "Saturn", 5.68e26, 58232e3, numpy.array([1.434e12, 0.0,0.0]), numpy.array([0.0, 9.6e3, 0.0]))
    uranus = Planet( "Uranus", 8.68e25, 25362e3, numpy.array([2.872e12, 0.0,0.0]), numpy.array([0.0, 6.8e3, 0.0]))
    neptun = Planet( "Neptun", 1.02e26, 24624e3, numpy.array([4.495e12, 0.0,0.0]), numpy.array([0.0, 5.43e3, 0.0]))
    
    sunsystem = [sun, merkur, venus, earth, mars, jupiter, saturn, uranus, neptun]
    
    numberOfSteps = 24*365    #numberOfSteps * timePerStep = durutation of the simulation
    timePerStep = 3600      #this value is in seconds
    
    planetNr = 3
    
    xList = list()
    yList = list()
    xList.append(sunsystem[planetNr].posVector[0])
    yList.append(sunsystem[planetNr].posVector[1])
    
    for i in xrange(numberOfSteps):
        sunsystem = mp.updateSunsystem(sunsystem, timePerStep)
        xList.append(sunsystem[planetNr].posVector[0])
        yList.append(sunsystem[planetNr].posVector[1])
        print "remaining steps ", numberOfSteps - i
        #print "x: ",sunsystem[planetNr].posVector," y: ",sunsystem[planetNr].posVector
        
    pylab.plot(xList, yList)
    pylab.xlabel('x')
    pylab.ylabel('y')
    pylab.show()