# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 16:38:11 2010

@author: falk
Dieser Test überprüft die Korrektheit der einzelnen Methoden.
"""
import sys
sys.path.append("../")
from dev.AstroCalc import *
import unittest

class TestAstroCalc(unittest.TestCase):
    """
    This class tests calculations of AstroClac
    """
    def testupdatePosition(self):
        """
        needed args: altePosition, zeitintervall, geschwindigkeit, beschleunigung
        """
        pass
    
    def testCumulativeMass(self):
        """
        test of this function
        """
        massesA = [1000, 2000, 3000, 4000, 5000]
        self.assertEqual(cumulativeMass(massesA), 15000)  

    def testWeightForce(self):
        """
        needed args: m1, m2, v1, v2
        """
        pass
    
    def totalPosition(self):
        """
        needed args: listOfMasses, listOfPositions
        """
        pass
        
    def magnitudeOfSpeed(self):
        """
        cumMass, singleMass, posSingle, posCenter
        """
        pass
    
        
if __name__ == '__main__':
    unittest.main()