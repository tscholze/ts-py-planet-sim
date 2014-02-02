# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 09:06:34 2010

@author: falk
"""
from __future__ import division
import numpy
import math
from Planet import Planet


def updatePosition(planet, zeitintervall, beschleunigung):
    """
    Berechnet die neue Position aus der Alten mit Hilfe von Geschwindigkeit und
    Beschleunigung.
    Taylor-Polynom
    @param altePosition Die urspruengliche Position des Koerpers
    @param zeitintervall das Zeitintervall in dem die Simulation aktualisiert wird
    @param geschwindigkeit die Geschwindigkeit mit der sich der Koerper bewegt
    @param beschleunigung die Beschleunigung des Koerpers
    @return die neue Position als Vektor
    
    >>> updatePosition(Planet(1, 500, 0, numpy.array([5, 7, 3]), 0), 1, 50)
    array([ 30.,  32.,  28.])
    >>> updatePosition(Planet(3, 900, 0, numpy.array([7, 8, 9]), numpy.array([1, 2, 3])), 1, 50)
    array([ 33.,  35.,  37.])
    >>> updatePosition(Planet(3, 900, 0, numpy.array([7, 8, 9]), numpy.array([1, 2, 3])), 5, 50)
    array([ 637.,  643.,  649.])
    """
    ergebnis = planet.posVector + (planet.veloVector * zeitintervall)
    ergebnis = ergebnis + ((zeitintervall ** 2) / 2)  * beschleunigung
    
    return ergebnis

def cumulativeMass(listOfPlanets):
    """
    Calculates the total mass of all given masses
    @param listOfMasses: A list that contains all the different masses
    @return totalMass: 
    
    >>> lop = list()
    >>> lop.append(Planet(1, 500, 0, numpy.array([5, 7, 3]), 0))
    >>> lop.append(Planet(2, 600, 0, numpy.array([1, 3, 5]), 0)) 
    >>> lop.append(Planet(3, 900, 0, numpy.array([7, 8, 9]), numpy.array([1, 2, 3])))
    >>> cumulativeMass(lop)
    2000
    """
    totalMass = 0
    
    for planet in listOfPlanets:
        totalMass += planet.mass
    
    return totalMass

def weightForce(planetA, planetB, g = 6.672e-11):
    """
    Berechnet die Gravitationskraft zweier aufeinander einwirkender
    Koerper im 3D-Raum
    @param planetA: first planet
    @param planetB: second planet
    @return: resulting gravity force
    
    >>> lop = list()
    >>> lop.append(Planet(1, 500, 0, numpy.array([5, 7, 3]), 0))
    >>> lop.append(Planet(2, 600, 0, numpy.array([1, 3, 5]), 0)) 
    >>> lop.append(Planet(3, 900, 0, numpy.array([7, 8, 9]), numpy.array([1, 2, 3])))
    >>> weightForce(lop[1],  lop[0])
    array([  3.70666667e-07,   3.70666667e-07,  -1.85333333e-07])
    """
    posDiff = planetB.posVector - planetA.posVector
    #print "pos Diff: ", posDiff
    a = ((numpy.linalg.norm(posDiff)) ** 3)
    #print "a: ", a
    massProduct = (planetA.mass * planetB.mass)
    #print "massProduct: ", massProduct
    erg = (g * ((massProduct / a) * posDiff))
    #print "Ergebnis ", erg
    return erg
    
def totalPosition(listOfPlanets):
    """
    Calculates the resulting position of all mass impulses.
    The order of the masses and the positions should be the same.
    @param listOfMasses: a list of all masses
    @param listOfPositions: a list of all positions as a numpy.array
    @return the center of mass as a new planet with a ID = -1
    
    >>> lop = list()
    >>> lop.append(Planet(1, 500, 0, numpy.array([5, 7, 3]), 0))
    >>> lop.append(Planet(2, 600, 0, numpy.array([1, 3, 5]), 0)) 
    >>> lop.append(Planet(3, 900, 0, numpy.array([7, 8, 9]), numpy.array([1, 2, 3])))
    >>> planet = totalPosition(lop)
    >>> planet.posVector
    array([ 4.7 ,  6.25,  6.3 ])
    """
    newPos = numpy.array([0, 0, 0])
    totalMass = cumulativeMass(listOfPlanets)
    
    for planet in listOfPlanets:
        newPos = newPos + planet.mass * planet.posVector
    newPos = newPos / totalMass
    
    return Planet(id = -1, mass = totalMass, radius = 0, posVector = newPos, veloVector = numpy.array([0, 0, 0]))
    
def acceleration(force, mass):
    """
    Calculates the acceleration through force devided by mass.
    @param force: force as a vector
    @param mass: mass as a numeric value. This should be not 0.
    @return: acc the acceleration
    
    >>> acceleration(300, 30)
    10.0
    """
    #print "mass: ", mass
    #print "force: ", force
    acc = force/mass
    return acc   
    
def directionOfSpeed(planet, restOfSystem):
    """
    Calculates the vector direction of the speed impulse.impuls
    The resulting vector has a magnitude of 1. Required are two vectors. The 
    resulting direction vector belongs the first one of the given vectors. In 
    many cases the second vector is the position of the restOfSystem of mass.
    @param positionA: The first position as a vector
    @param positinoB: The second position as a vector
    @return: the direction vector with a magnitude of 1
    
    >>> lop = list()
    >>> lop.append(Planet(1, 500, 0, numpy.array([5, 7, 3]), 0))
    >>> lop.append(Planet(2, 600, 0, numpy.array([1, 3, 5]), 0)) 
    >>> lop.append(Planet(3, 900, 0, numpy.array([7, 8, 9]), numpy.array([1, 2, 3])))
    >>> totalRestPos = totalPosition(lop[1:])
    >>> directionOfSpeed(lop[0], totalRestPos)
    array([ 0.92847669, -0.37139068,  0.        ])
    """
    z = numpy.array([0, 0, 1])
    vecDiff = planet.posVector - restOfSystem.posVector
    crossProduct = numpy.cross((vecDiff), z)
    down = numpy.linalg.norm(crossProduct)
    erg = crossProduct / down
    return erg
    
def magnitudeOfSpeed(planet, centerOfMass, restOfSystem, g = 6.672E-11):
    """
    @param planet: planet
    @param centerOfMass: center of mass
    @param restOfSystem: the rest of the system without 'planet'
    @return: magnitude of the speed vector
    """
    pos = numpy.linalg.norm(planet.posVector - restOfSystem.posVector)
    result = math.sqrt((g * centerOfMass.mass) / pos)
    result = ((centerOfMass.mass - planet.mass) / centerOfMass.mass) * result
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
