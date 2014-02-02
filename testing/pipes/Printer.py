'''
Created on Dec 18, 2010

@author: falk
'''

import threading
import multiprocessing

class Printer(multiprocessing.Process):
    '''
    This class prints a object. At one point it receives a new version of this object.
    Then it will replace the old object with the new one an it will print this.
    '''
    

    def __init__(self, myEndOfThePipe, objectToPrint):
        '''
        Constructor
        '''
        self.__pipe = myEndOfThePipe
        self.__object = objectToPrint
        #multiprocessing.Process.__init__(target=self)
        super(Printer, self).__init__()
        
    def printObject(self):
        #print "i am here"
        while True:
            if self.__object == 'end':
                print "finished!"
                break
            print "received: ", self.__object
    
    def run(self):
        p = threading.Thread(target=self.getNewObject)
        p.start()
        self.printObject()
         
    def getNewObject(self):
        while True:
            newObj = self.__pipe.recv()
            self.__object = newObj