"""
    Copyright (C) 2021  CNRS
    This file is part of "Speedlib".
    "Speedlib" is an API built for the use case of autonomous navigation.
    It has  been developed to control quay cranes and trains of multimodal
    waterborne Lab as part of The SPEED project, a project which aims to
    enhance and support the growth of a system of connected port solutions,
    with the use of data science and IoT (Internet of Things) technologies.
    The library allows controlling the motion of the IoT devices at H0 scale
    in automatic mode, in three directions and exchanging with the information
    system for overall management
"""
# -*-coding: <Utf-8> -*-
from speedlib.dcc import dcc_object
from speedlib.dcc.dcc_object import DCCObject

class Switch():
    """ This class is used to control Servo motors """
    def __init__(self, name, adress):
        """
        Parameters
        ----------
        name : string
            DESCRIPTION : It is the name of the train
        adress : int
            DESCRIPTION This is the address on which it was programmed
        Returns
        -------
        None.

        """
        if not isinstance(name, str):
            raise TypeError(" name must be a str but got " +str(name))
        if not isinstance(adress, int):
            raise TypeError("adress must be an integer but got  " +str(adress))
        #if adress not in range(101, 126):
            #raise RuntimeError("""The address must be between 101 and 125 but got """+str(adress))
        self.dccobject = DCCObject(name, adress)


    def _get_biais_one(self):
        """
        Returns
        -------
        TYPE
            DESCRIPTION : Returns the current state of the switch

        """
        return self.dccobject.f1

    def _set_biais_one(self, var):
        """
        Parameters
        ----------
        var : Boolean
            DESCRIPTION : change the state of the switch

        Returns
        -------
        None.

        """
        if not isinstance(var, bool):
            raise TypeError(" var must me a boolean but got "+str(var))
        self.dccobject.f1 = var

    biais_one = property(_get_biais_one, _set_biais_one)

    def _get_biais_two(self):
        """
        Returns
        -------
        TYPE
            DESCRIPTION : Returns the current state of the switch

        """
        return self.dccobject.f2, self.dccobject.fl

    def _set_biais_two(self, var):
        """
        Parameters
        ----------
        var : Boolean
            DESCRIPTION : change the state of the switch

        Returns
        -------
        None.

        """
        if not isinstance(var, bool):
            raise TypeError(" var must me a boolean but got "+str(var))
        self.dccobject.f2 = var
        if var is True:
            self.dccobject.fl = var
        if var is False:
            self.dccobject.reverse()

    biais_two = property(_get_biais_two, _set_biais_two)




if __name__ == "__main__":
    S = Switch("DCC3", 3)
    dcc_object.start()
    S.biais_one = True
    S.biais_two = True
    dcc_object.stop()
