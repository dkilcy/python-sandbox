'''
Created on Apr 17, 2014

@author: dkilcy
'''

class EntryExit(object):
    '''
    classdocs
    '''
    
    def __init__(self, params):
        '''
        Constructor
        '''
        self.f = params
        
    def __call__(self):
        print("Entering %s" % (self.f.__name__))
        self.f()
        print("Exiting %s" % (self.f.__name__))
        
@EntryExit
def func1():
    print("inside func1()")
    
@EntryExit
def func2():
    print("inside func2()")
    
func1()
func2()
