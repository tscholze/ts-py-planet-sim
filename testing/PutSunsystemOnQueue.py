'''
Created on 17.12.2010

@author: falk

Füllt den Movement mit vielen Jobs um die Queue unter Last zu bringen.
Schreibt die erhaltenen Ergebnisse auf die Console.
'''
from PlanetSim.dev.distributed_computing.Master import Movement
from PlanetSim.dev.distributed_computing.Movement import Movement
from PlanetSim.dev import EarthSunsystemCalc

if __name__ == '__main__':
    m = Movement()
    mv = Movement(m)
    newSystem = EarthSunsystemCalc.generate_our_sunsystem()
    for i in range(10000):
        newSystem = mv.updateSunsystem(newSystem)
        print "will print new System: "
        for planet in newSystem:
            print "newPlanet", planet.id
        print "finished printing new system"
        print "=============================================="