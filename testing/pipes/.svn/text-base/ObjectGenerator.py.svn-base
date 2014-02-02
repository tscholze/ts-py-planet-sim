'''
Created on Dec 18, 2010

@author: falk
'''
import time, random, multiprocessing
class ObjectGenerator(multiprocessing.Process):
    '''
    Generates new objects that will be printed.
    '''


    def __init__(self, myEndOfThePipe, objectToPrint = 1):
        '''
        Constructor
        '''
        self.__pipe = myEndOfThePipe
        self.__object = objectToPrint
        #multiprocessing.Process.__init__(target=self)
        super(ObjectGenerator, self).__init__()
        
    def generateNewObj(self):
        while self.__object < 10:
            self.__object = self.__object + 1
            print "will write ", self.__object
            self.__pipe.send(self.__object)

            time.sleep(random.normalvariate(.9, .1))
        time.sleep(20)
        self.__pipe.send(20)
        self.__pipe.send('end')
            
    def run(self):
        self.generateNewObj()