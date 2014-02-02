# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 16:10:32 2010

@author: falk

Berechnet die Flugbahn der Erde um die Sonne. Die Sonne ist fest und nur die Erde bewegt sich.
"""

import sys
sys.path.append("../")
import PlanetSim.dev.AstroCalc as ac
import numpy
import pylab

m1 = 5.97e24 #mass of the test planet
m2 = 1e38 #mass of the center 2.054e40
pos1 = numpy.array([149.6e9,0.0,0.0]) #position of the test planet
pos2 = numpy.array([0, 0, 0]) # position of the center

v1 = numpy.array([0.0,29.8e3,0.0]) #Anfangsgeschwindigkeit

time = 0.01 #Zeitintervall für die Berechnung (dt)

x = list() #Liste aller x-Koordinaten
y = list() #Liste aller y-Koordinaten

"""
In dieser vereinfachten Simulation ist der Körper 2 fest. Eigentlich muss diese
Berechnung für alle Körper durchgeführt werden.
"""
for i in range(100000):
    #Berechnnung der Gravitationskraft zwischen den beiden Körpern
    force = ac.weightForce(m1, m2, pos1, pos2)
    #print "force: ", force
    #Berechnung der Beschleunigung
    acc = ac.acceleration(force, m1)
    #print "acc: ", acc
    #v1 = v1 + acc * time
    #Ermittle neue Position. Das ist das Taylor-Polynom
    pos1 = ac.updatePosition(pos1, time, v1, acc)

    v1 = ac.directionOfSpeed(pos1, pos2) * ac.magnitudeOfSpeed(m1+m2, m1, pos1, m2*pos2)
    #Anfügen der beiden Koordinaten an die jeweiligen Listen.
    x.append(pos1[0])
    y.append(pos1[1])

#Listen zuweisen und zeichnen
pylab.plot(x, y)
pylab.xlabel('x')
pylab.ylabel('y')
pylab.show()