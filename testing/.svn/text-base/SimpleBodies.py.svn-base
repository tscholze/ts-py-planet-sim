# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 16:10:32 2010

@author: falk

Diese Klasse berechnet die Flugbahn zweier Körper.
"""

import sys
sys.path.append("../")
import PlanetSim.dev.AstroCalc as ac
import numpy
import pylab

m1 = 9 #mass of the test planet
m2 = 9e9 #mass of the center
r1 = numpy.array([1, 0, 0]) #position of the test planet
r2 = numpy.array([0, 0, 0]) # position of the center

v1 = numpy.array([0, 1, 0]) #Anfangsgeschwindigkeit

time = 0.01 #Zeitintervall für die Berechnung (dt)

x = list() #Liste aller x-Koordinaten
y = list() #Liste aller y-Koordinaten

"""
In dieser vereinfachten Simulation ist der Körper 2 fest. Eigentlich muss diese
Berechnung für alle Körper durchgeführt werden.
"""
for i in range(100000):
    #Berechnnung der Gravitationskraft zwischen den beiden Körpern
    force = ac.weightForce(m1, m2, r1, r2)
    #Berechnung der Beschleunigung
    acc = ac.acceleration(force, m1)
    #Ermittle neue Position. Das ist das Taylor-Polynom
    r1 = ac.updatePosition(r1, time, v1, acc)
    """
    Nun muss die neue Geschwindigkeit ausgerechnet werden. Sie besteht aus 2 Teilen,
    ihrem Richtungsvektor und ihrer Länge. Ihr neuer Richtugnsvektor kann durch
    die Formel Nr.9 bestimmt werden, das ist directionOfSpeed. Dieser Vektor hat
    allerdings die Länge 1. Deshalb muss noch der Betrag des Vektors berechnet
    werden. Das geschiet mit magnitudeOfSpeed, der Formel Nr. 8. Körper 2 wird 
    vereinfacht als Massenschwerpunkt angenommen.
    """
    v1 = ac.directionOfSpeed(r1, r2) * ac.magnitudeOfSpeed(m1+m2, m1, r1, m2*r2)
    #Anfügen der beiden Koordinaten an die jeweiligen Listen.
    x.append(r1[0])
    y.append(r1[1])

#Listen zuweisen und zeichnen
pylab.plot(x, y)
pylab.xlabel('x')
pylab.ylabel('y')
pylab.show()