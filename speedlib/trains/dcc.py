# -*-coding: <Utf-8> -*-
from dccpi import *


e = DCCRPiEncoder()
controller = DCCController(e)
def start():
    controller.start()
def stop():
    controller.stop()



class Train:
    def __init__(self, name, adress):
        
        if not isinstance(name, str):
            raise TypeError(" name must be a str but got " +str(name))
        if not isinstance(adress, int):
            raise TypeError("adress must be an integer but got  " +str(adress))
        if adress < 1 and adress >127:
            raise RuntimeError("The address must be between 1 and 127 but preferably 3 which is the factory address but got "+str(adress))
        
        self.name = name   
        self.adress = adress
        self.l = DCCLocomotive(name,adress)
        controller.register(self.l)
        self._speed = 0
        self._fl = False
        self._f1 = False
        self._f2 = False
        self._f3 = False
        self._f4 = False
            
    def reverse(self):
        """Change the direction"""
        self.l.reverse()  
        
    def faster(self):
        """ Increase 1 speed step"""
        self.l.faster()
        
    def slower(self):
        """Reduce the speed"""
        self.l.slower()
        
    def _set_speed(self,new_speed):
        """This function allow us to change the speed"""
        if not isinstance(new_speed, int):
            raise TypeError("vew_speed must be an integer but get "+ str(new_speed))
        self.l.speed = new_speed
    speed = property(_set_speed)
            
    def _set_fl(self,x):
        if x not in [False, True]:
            raise TypeError("x must be a bool but got "+str(x))
        self.l._fl = x
    fl = property(_set_fl)
    
    def _set_f1(self,x):
        if not isinstance(x, bool):
            raise TypeError("x must be a bool but got "+str(x))
        self.l._f1 = x
    f1 = property(_set_f1)
    
    def _set_f2(self,x):
        if not isinstance(x, bool):
            raise TypeError("x must be a bool but got "+str(x))
        self.l._f2 = x
    f2 = property(_set_f2)
    
    def _set_f3(self,x):
        if not isinstance(x, bool):
            raise TypeError("x must be a bool but got "+str(x))
        self.l._f3 = x
    f3 = property(_set_f3)
    
    def _set_f4(self,x):
        if not isinstance(x, bool):
            raise TypeError("x must be a bool but got "+str(x))
        self.l._f4 = x
    f4 = property(_set_f4)
