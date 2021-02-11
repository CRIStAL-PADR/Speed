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
            
    def reverse(self):
        """Change the direction"""
        self.l.reverse()  
     
    def stop(self):
        """ Emergency stop. stop controller always"""
        self.l.stop()
        
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
            
    def fl(self,x):
        self.l.fl = x
        
    def f1(self,x):
        self.l.f1 = x
        
    def f2(self,x):
        self.l.f2 = x
        
    def f3(self,x):
        self.l.f3 = x
    
    def f4(self,x):
        self.l.f4 = x
