import dcc_object
from dcc_object import DCCObject

class Train:
    def __init__(self, name, adress):
        """ this function takes a name and an address (an integer # 0) as
        parameters to create a train and  register it  on the controller
        """
        if not isinstance(name, str):
            raise TypeError(" name must be a str but got " +str(name))
        if not isinstance(adress, int):
            raise TypeError("adress must be an integer but got  " +str(adress))
        if adress not in range(1, 100):
            raise RuntimeError("""The address must be between 1 and 127 but
              got """+str(adress))
        self.dccobject = DCCObject(name, adress)
    
    def faster(self):
        self.dccobject.faster()
        
    def reverse(self):
        """Change the direction"""
        self.dccobject.reverse()
    
    def slower(self):
        """Reduce the speed"""
        self.dccobject.slower()
    
    def __repr__(self):
        return self.dccobject.__repr__()
        
    def _get_speed(self):
        """ Returns the current speed of the train """
        return self.dccobject.speed
    
    def _set_speed(self, new_speed):
        """ change the speed"""
        self.dccobject.speed = new_speed
    speed = property(_get_speed, _set_speed)
        
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
    
    train1 = Train("DCC3",99)
    train1.speed = 15
    train1.fl = True
    print(train1)