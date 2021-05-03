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
        if adress not in range(101, 126):
            raise RuntimeError("""The address must be between 1 and 127 but preferably 3
             which is the factory address but got """+str(adress))
        self.dccobject = DCCObject(name, adress)


    def _get_biais(self):
        """Returns the current state of the switch """
        return self.dccobject.f1

    def _set_biais(self, var):
        """ change the state of the switch """
        self.dccobject.f1 = var
    biais = property(_get_biais, _set_biais)
    

if __name__ == "__main__":
    S = Switch("DCC", 102)
    dcc_object.start()
    S.biais = True
    dcc_object.stop()