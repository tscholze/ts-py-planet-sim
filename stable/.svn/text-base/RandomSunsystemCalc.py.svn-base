# -*- coding: utf-8 -*-
"""

"""
import numpy
from Planet import Planet
import random
import math
import AstroCalcPlanetClass as ac

def generate_random_system(amount_bodies, sun_mass_factor, planet_mass_min, 
                            planet_mass_max, planet_radius_min, planet_radius_max, 
                            planet_orbit_min, planet_orbit_max):
    """
    Generates random objects by the given parameters.
    @param amount_bodies: the number of the objects that will be created
    @param sun_mass_factor: the mass of the center of the system relative to the sun's mass
    @param planet_mass_min: the minimum of the mass a object will have
    @param planet_mass_max: the maximum of the mass a object will have
    @param planet_radius_min: the minimum of the radius a object will have. NOTE: This will have no effect on the calculation. It's only for rendering reasons.
    @param planet_radius_max: the maximum of the radius a object will have
    @param planet_orbit_min: the minimum of the system's width
    @param planet_orbit_max: the maximum of the system's width
    @return: a celestial system
    """
    list_of_planets = []
        
    # Sun Data
    sun_mass = 2.054e30 * int(sun_mass_factor)
    sun_radius = 696e6
    sun_velo = numpy.array([1e-10, 1e-10, 1e-10])
    sun_pos = numpy.array([0, 0, 0])
    # Sun has always the ID 0
    list_of_planets.append(Planet(0 , sun_mass, sun_radius, sun_velo, sun_pos))

    i = 1
    while i < amount_bodies:
        random_mass = int(random.randrange(planet_mass_min, planet_mass_max, 1))*1e23
        random_radius = random.randrange(planet_radius_min, planet_radius_max, 1)*1e3
        xPos = random.randrange(planet_orbit_min, planet_orbit_max, 1)
        random_posVector = numpy.array([xPos, getYposOfVector(xPos) ,0])*1e9
        random_veloVector = numpy.array([0,random.randrange(1, 100, 1), 0])*1e3
        random_planet = Planet(i , random_mass, random_radius, random_posVector, random_veloVector)          
        list_of_planets.append(random_planet)
        i += 1

    setStableSpeed(list_of_planets)
    
    return list_of_planets

def getYposOfVector(xPos):
    """
    Creates a new position on the y axis by using the math.tan function. 
    @param xPos: the position on the x axis
    @return: the position on the y axis
    """
    return math.tan(random.uniform(0, 2 * math.pi)) * xPos

def setStableSpeed(system):
    """
    Creates a velocity vector so that the system is 'stable'.
    @param system: the whole system
    @return: a velocity vector for a planet
    """
    centerOfMass = ac.totalPosition(system)     
    for planet in system:
            restOfSystem = list()
            
            for p in system:
                if p is not planet:
                    restOfSystem.append(p)
                    
            restOfSystem = ac.totalPosition(restOfSystem)
            newDirection = ac.directionOfSpeed(planet, restOfSystem)
            newMagnitude = ac.magnitudeOfSpeed(planet, centerOfMass, restOfSystem)
            newSpeed = newDirection * newMagnitude
            planet.veloVector = newSpeed
        
        
