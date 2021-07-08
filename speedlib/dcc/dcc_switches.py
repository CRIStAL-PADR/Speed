"""
    Created on Tue May 4 2021
"""
# -*-coding: <Utf-8> -*-
import dcc_object
from dcc_object import DCCObject

class Switch(object):
    """
        Switch class
    """
    def __init__(self, name, adress):
        """
            this function takes a name and an address (an integer # 0) as
			parameters to create a train and  register it  on the controller
        """
        if not isinstance(name, str):
            raise TypeError(" name must be a str but got " +str(name))
        if not isinstance(adress, int):
            raise TypeError("adress must be an integer but got  " +str(adress))
        #if adress not in range(101, 126):
            #raise RuntimeError("""The address must be between 101 and 125 but got """+str(adress))
        self.dccobject = DCCObject(name, adress)


    def _get_biais1(self):
        """Returns the current state of the switch """
        return self.dccobject.f1

    def _set_biais1(self, var):
        """ change the state of the switch """
        self.dccobject.f1 = var
    biais1 = property(_get_biais1, _set_biais1)
    
    def _get_biais2(self):
        """Returns the current state of the switch """
        return self.dccobject.f2

    def _set_biais2(self, var):
        """ change the state of the switch """
        self.dccobject.f2 = var
    biais2 = property(_get_biais2, _set_biais2)
    
    def _get_light_1(self):
        """ return the current state of the light 1"""
        return self.dccobject.fl
    
    def _set_light_1(self, var):
        """ change the state of the light 1 """
        self.dccobject.fl = var
    light_1 = property(_get_light_1, _set_light_1)
    
    def light_2(self):
        """ change the state of the light 2 """
        self.dccobject.reverse()
        
    
     

if __name__ == "__main__":
    S = Switch("DCC3", 3)
    dcc_object.start()
    S.biais1 = True
    S.biais2 = True
    S.light_1 = True
    print(S.light_1)
    #dcc_object.stop()
