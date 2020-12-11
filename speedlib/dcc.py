from dccpi import *

class Train (): 
   
    
    def initialisation(self):
        """ Cette fonction permet de faire l'initialisation en créant un DCC controller avec
        le RPI encoder"""
        e = DCCRPiEncoder()
        controller = DCCController(e) # Create the DCC controller with the RPi encoder

    def register(self):
        """This function create a locos, agrgs : Name , DCC Adress"""    
        
    
    
    if __name__ == "main" :
        
        initialisation () # permet de créer le controller DCC avec le RPi encoder
        register(l1)
        
