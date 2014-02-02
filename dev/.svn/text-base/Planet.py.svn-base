# -*- coding: utf-8 -*-
'''
Created on 13.11.2010

@author: tobias
'''

import numpy

class Planet(object):
    '''
    A Planet-Object stores all relevant information which are relevant
    for calculating the galaxy.
    '''

    id = 0
    mass = 0.0
    radius = 0.0
    posVector = numpy.array([0,0,0])
    veloVector = numpy.array([0,0,0])
    name = ""
    
    
    def __init__(self, id, mass, radius, posVector, veloVector, name = "auto"):
        '''
        Set values
        @param m: Planets mass
        @param r: Radius
        @param pos: Position as vector
        @param v: Velocity as vector    
        '''
        self.id = id
        self.mass = mass
        self.radius = radius
        self.posVector = posVector
        self.veloVector = veloVector
        self.name = name
        
    def get_posVector_x(self):
        return self.posVector[0]
    
    def get_posVector_y(self):
        return self.posVector[1]
    
    def get_posVector_z(self):
        return self.posVector[2]
    
    def get_radius(self):
        return self.radius
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        """
        Creates a string representation of the planet.
        This is mainly for debugging purpose.
        """
        str = "This Planet has a ID of %s\n\ta mass of %s\n\ta radius of %s\n\tIts position is %s\n\tand its speed vector is %s" %( self.id, self.mass,  self.radius, self.posVector, self.veloVector)
        return str
    
    def __cmp__(self, planet):
        """
        Proofs whether planet has the same id as self.
        """
        #return self.id == planet.id
        pass