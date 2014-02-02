'''
Created on 13.11.2010

@author: tobias

Sammlung von astronomischen und physikalischen Berechnung
passend zur Planeten Simulation
'''

import numpy
import math
from papyon.util.decorator import deprecated


def updatePosition(altePosition, zeitintervall, geschwindigkeit, beschleunigung):
    """
    Berechnet die neue Position aus der Alten mit Hilfe von Geschwindigkeit und
    Beschleunigung
    @param altePosition Die urspruengliche Position des Koerpers
    @param zeitintervall das Zeitintervall in dem die Simulation aktualisiert wird
    @param geschwindigkeit die Geschwindigkeit mit der sich der Koerper bewegt
    @param beschleunigung die Beschleunigung des Koerpers
    @return die neue Position als Vektor
    """
    ergebnis = altePosition + (geschwindigkeit * zeitintervall)
    ergebnis += ((zeitintervall ** 2) / 2)  * beschleunigung
    
    return ergebnis

def cumulativeMass(listOfMasses):
    """
    Calculates the total mass of all given masses
    @param listOfMasses: A list that contains all the different masses
    @return totalMass: 
    """
    totalMass = 0
    """
    for planet in listOfPlanets:
        totalMass += planet.mass
    """
    for mass in listOfMasses:
        totalMass += mass
    return totalMass

def weightForce(m1, m2, v1, v2, g = 6.672E-11):
    """
    Berechnet die Gravitationskraft zweier aufeinander einwirkender
    Koerper im 3D-Raum
    @param m1 Masse des ersten Koerpers
    @param m2 Masse des zweitesn Koerpers
    @param v1 Lagevektor des ersten Koerpers
    @param v2 Lagevektor des zweiten Vektors
    @return resultierender Kraftvektor
    """
    return g*(((m1*m2)/(numpy.linalg.norm(v2-v1)**3))*(v2-v1))
    
def totalPosition(listOfMasses, listOfPositions):
    #def totalPosition(listOfPlanets):
    """
    Calculates the resulting position of all mass impulses.
    The order of the masses and the positions should be the same.
    @param listOfMasses: a list of all masses
    @param listOfPositions: a list of all positions as a numpy.array
    @return
    """
    result = numpy.array([0, 0, 0])
    for mass, position in listOfMasses, listOfPositions:
        result += position * mass
    result /= cumulativeMass(listOfMasses)
    """
    for planet in listOfPlanets:
        result += planet.mass * planet.posVector
        result /= cumulativeMass(listOfPlanets)
    """
    return result
    
def acceleration(force, mass):
    """
    Calculates the acceleration through force devided by mass.
    @force: force as a vector
    @mass: mass as a numeric value. This should be not 0.
    """
    return force/mass    
    
def directionOfSpeed(positionA, positionB):
    """
    Calculates the vector direction of the speed impulse.impuls
    The resulting vector has a magnitude of 1. Required are two vectors. The 
    resulting direction vector belongs the first one of the given vectors. In 
    many cases the second vector is the position of the center of mass.
    @param positionA: The first position as a vector
    @param positinoB: The second position as a vector
    @return: the direction vector with a magnitude of 1
    """
    up = numpy.cross((positionA - positionB), [0, 0, 1])
    down = numpy.linalg.norm(numpy.cross((positionA - positionB), [0, 0, 1]))

    return up/down
    
def magnitudeOfSpeed(cumMass, singleMass, posSingle, posCenter, g = 6.672E-11):
    """
    @param cumMass: mass of celectrial bodies
    @param singleMass: mass of the affected object
    @param posSingle: positino of the object
    @param posCenter: position of the mass center
    @return: magnitude of the speed vector
    """
    pos = numpy.linalg.norm(posSingle - posCenter)
    #print "pos: ",pos
    result = math.sqrt((g * cumMass) / pos)
    result = (float(cumMass - singleMass) / float(cumMass)) * result
    #print "(cumMass - singleMass)/ cumMass", (cumMass - singleMass)
    return result
    
@deprecated
def selftest():
    """
    deprecated
    Runs a selftest on this class
    
    1. Berechne Kraft
    2. Berechne Beschleunigung
    3. Berechne neue Position
    4. Berechne neue Geschwindigkeit
    """
    
    planets = []
    
    from Planet import Planet
    
    earth = Planet(1, 1.0, 1.0, numpy.array([3,3,3]), numpy.array([5,0,0]))
    sun = Planet(2, 1000.0, 10.0, numpy.array([1,1,1]), numpy.array([0,0,0]))
    
    planets.append(earth)
    planets.append(sun)
    
    print "Masse: ",cumulativeMass(planets)
    
    
    #force = weightForce(sun.mass, earth.mass, sun.posVector, earth.posVector, g = 6.672E-11)
    #acc = acceleration(force, earth.mass)
    #newPos = updatePosition(earth.posVector, 0.01, earth.veloVector, acc)
         
