# -*- coding: utf-8 -*-
'''
Created on 18.11.2010

@author: falk

Dieser Test überprüft die Korrektheit der einzelnen Methoden.
'''
from __future__ import division
import sys
sys.path.append("../")
from PlanetSim.dev.Planet import Planet
import PlanetSim.dev.AstroCalcPlanetClass as ac
import unittest
import numpy
import math


class Test(unittest.TestCase):
    def setUp(self):
        self.lop = list()
        self.lop.append(Planet(1, 500, 0, numpy.array([5, 7, 3]), 0))
        self.lop.append(Planet(2, 600, 0, numpy.array([1, 3, 5]), 0)) 
        self.lop.append(Planet(3, 900, 0, numpy.array([7, 8, 9]), numpy.array([1, 2, 3])))

    def testCumulativeMass(self):
        tm = ac.cumulativeMass(self.lop)
        self.assertEqual(tm, 2000)
        
    def testTotalPosition(self):
        tp = ac.totalPosition(self.lop)
        self.assertEqual(tp.posVector[0], 4)
        self.assertEqual(tp.posVector[1], 6)
        self.assertEqual(tp.posVector[2], 6)
        
    def testWeightForce(self):
        tw = ac.weightForce(self.lop[0], self.lop[1])
        self.assertEqual(all(tw), all(numpy.array([3.70666667e-07, 3.70666667e-07,-1.85333333e-07])))
        
    def testUpdatePosition(self):
        tup = ac.updatePosition(self.lop[0], 1, 50)
        self.assertEqual(tup[0], 30)
        self.assertEqual(tup[1], 32)
        self.assertEqual(tup[2], 28)
        
        tup = ac.updatePosition(self.lop[2], 1, 50)
        self.assertEqual(tup[0], 33)
        self.assertEqual(tup[1], 35)
        self.assertEqual(tup[2], 37)
        
        tup = ac.updatePosition(self.lop[2], 5, 50)
        self.assertEqual(tup[0], 637)
        self.assertEqual(tup[1], 643)
        self.assertEqual(tup[2], 649)
        pass
    
    def testAcceleration(self):
        ta = ac.acceleration(1000, self.lop[0].mass)
        self.assertEqual(ta, 2)
    
    def testDirectionOfSpeed(self):
        totalRestPos = ac.totalPosition(self.lop[1:])
        tds = ac.directionOfSpeed(self.lop[0], totalRestPos)
        self.assertEqual(tds[0], (1/math.sqrt(2)))
        self.assertEqual(tds[1], (-1/math.sqrt(2)))
        self.assertEqual(tds[2], 0)
    
    def testMagnitudeOfSpeed(self):
        totalpos = ac.totalPosition(self.lop)
        totalRestPos = ac.totalPosition(self.lop[1:])
        tmos = ac.magnitudeOfSpeed(self.lop[0], totalpos, totalRestPos)
        #self.assertEqual(tmos, ((3/4)*math.sqrt((2000*6.672E-11)/math.sqrt(1.16))))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()