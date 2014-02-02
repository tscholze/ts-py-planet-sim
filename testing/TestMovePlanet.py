'''
Created on 28.11.2010

@author: falk

Tests all methods of MovePlanet.
'''
import unittest
import numpy

import sys
from PlanetSim.dev.MovePlanet import updateSunsystem
sys.path.append("../")

import PlanetSim.dev.MovePlanet
from PlanetSim.dev.Planet import Planet

class Test(unittest.TestCase):


    def setUp(self):
        self.simpleSys = list()
        self.simpleSys.append(Planet(0, 1, 1, numpy.array([0,0,0]), numpy.array([0,0,0])))
        self.simpleSys.append(Planet(1, 1, 1, numpy.array([0,0,0]), numpy.array([0,0,0])))
        self.simpleSys.append(Planet(2, 1, 1, numpy.array([0,0,0]), numpy.array([0,0,0])))


    def tearDown(self):
        pass


    def testCorrectOrder(self):
        """
        All planet of the system should return in the same order as they were created.
        """
        newSystem = updateSunsystem(self.simpleSys, 1)
        for i in range(3):
            self.assertEqual(self.simpleSys[i].id, newSystem[i].id)
            
    def testSystemWithOnlyOnePlanet(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()