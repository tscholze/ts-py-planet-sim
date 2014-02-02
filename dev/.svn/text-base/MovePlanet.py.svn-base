# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 08:50:30 2010

@author: falk
"""
from __future__ import division
import AstroCalcPlanetClass as ac
from Planet import Planet
import numpy


def calcNewPosForPlanet(currentPlanet, currentSunsystem, currentTimestep, MaxDistancePerStep):
    """
    Calculates the new position for the currentPlanet in the currentSunsystem. If one object is moving too fast, its steps
    will be seperated into smaller ones. So its position is more accurate due to its fast movement.
    @param currentPlanet: the currentPlanet
    @param currentSunsystem: the whole currentSunsystem, must be iterateable!
    @param currentTimestep: the currentTimestep step
    @return: the tuple of the coordinates
    """

    restOfSunsystem = list()
    for cb in currentSunsystem:
        if currentPlanet is not cb:
            restOfSunsystem.append(cb)

    newPlanet = calcNewPlanet(currentPlanet, currentTimestep, restOfSystem= restOfSunsystem)
    distance = numpy.linalg.norm(currentPlanet.posVector - newPlanet.posVector)
    
    if (distance > MaxDistancePerStep):
        """
        Nach der Gleichung currentTimestep/distance = newTimeStep/MAX_DISTANCE_PER_STEP
        kann der neue Zeitabschnitt berechnet werden.
        """
        newPlanet = currentPlanet
        newTimeStep = (currentTimestep / distance) * MaxDistancePerStep
        numberOfSteps = currentTimestep / newTimeStep
        #if (numberOfSteps > 100):
        #    print "unterteile Weg in ", numberOfSteps, " Schritte für den Planeten ", currentPlanet.id
        for i in xrange(long(numberOfSteps)):
            newPlanet = calcNewPlanet(newPlanet, newTimeStep, restOfSystem= restOfSunsystem)
    return newPlanet

def calcNewPlanet(planetToMove, timestep, restOfSystem):
    """
    Calculates the values of a celestial body that changes while moving.
    This method will be called several times when a object is moving too fast.
    @param planetToMove: the object that moves
    @param timestep: the timestep that elapses in every step
    @param centerOfMass: the mass that influences the speed
    @return: the new Planet 
    """
    
    gForce = numpy.array([0, 0, 0])
    for otherPlanet in restOfSystem:
        gForce = gForce + ac.weightForce(planetToMove, otherPlanet)
    acc = ac.acceleration(gForce, planetToMove.mass)
    newPos = ac.updatePosition(planetToMove, timestep, acc)
    
    newSpeed = (acc * timestep) + planetToMove.veloVector
    
    newPlanet = Planet(planetToMove.id, planetToMove.mass, planetToMove.radius, newPos, newSpeed)
    
    return newPlanet
    
def updateSunsystem(sunsystem, time = 1, MaxDistancePerStep = 1e9):
    """
    Calculates a new system with one function
    @param sunsystem: the original system
    @param time: the time that elapses with every step, the default value is 1 (second)
    @return: the new system
    """
    newSunsystem = list()
    for planet in sunsystem:
        newPlanet = calcNewPosForPlanet(planet, sunsystem, time, MaxDistancePerStep)          
        newSunsystem.append(newPlanet)
    return newSunsystem
    