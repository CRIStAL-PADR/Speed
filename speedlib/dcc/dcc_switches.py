import dcc_object
from dcc_object import DCCObject

class Switch:
    def __init__(self, name, adress):

        if not isinstance(name, str):
            raise TypeError(" name must be a str but got " +str(name))
        if not isinstance(adress, int):
            raise TypeError("adress must be an integer but got  " +str(adress))
        if adress not in range(101, 126):
            raise RuntimeError("""The address must be between 1 and 127 but preferably 3
             which is the factory address but got """+str(adress))
        self.dccobject = DCCObject(name, adress)

    def __repr__(self):
        return self.dccobject.__repr__()
        
    def _get_fl(self):
        """Returns the current state of fl """
        return self.dccobject.fl

    def _set_fl(self, var):
        """ change the state of fl """
        self.dccobject.fl = var
    fl = property(_get_fl, _set_fl)
    
    def _get_f1(self):
        """Returns the current state of f1 """
        return self.dccobject.f1

    def _set_f1(self, var):
        """ change the state of f1 """
        self.dccobject.f1 = var
    f1 = property(_get_f1, _set_f1)
    
    def _get_f2(self):
        """Returns the current state of f1 """
        return self.dccobject.f1

    def _set_f2(self, var):
        """ change the state of f1 """
        self.dccobject.f2 = var
    f2 = property(_get_f2, _set_f2)
    
    def _get_f3(self):
        """Returns the current state of f1 """
        return self.dccobject.f3

    def _set_f3(self, var):
        """ change the state of f1 """
        self.dccobject.f3 = var
    f3 = property(_get_f3, _set_f3)
    
    def _get_f4(self):
        """Returns the current state of f1 """
        return self.dccobject.f4

    def _set_f4(self, var):
        """ change the state of f1 """
        self.dccobject.f4 = var
    f4 = property(_get_f4, _set_f4)
    
    
    
    

if __name__ == "__main__":
    
    Switch = Switch("DCC3",102)
    Switch.speed = 15
    Switch.fl = True
    print(Switch.fl)
