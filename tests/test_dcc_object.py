import unittest
from speedlib.dcc import dcc_object
from speedlib.dcc.dcc_object import DCCObject



class TestDCCObject(unittest.TestCase):
    
    def test_init_with_invalid_adress(self):
        """Check that init returns an error when entering an invalid parameter""" 
        with self.assertRaises(TypeError):
            DCCObject("DCC1", "ad")
            dcc_object.start()
            dcc_object.stop()
            
    def test_init_with_invalid_name(self):
        """Check that init returns an error when entering an invalid parameter"""
        with self.assertRaises(TypeError):
            DCCObject(41, 5)
            dcc_object.start()
            dcc_object.stop()
            
    def test_init_with_valid_adress_name(self):
         """ Test that the init function works when a correct adress and name are  given""" 
         DCCObject("DCC1",1)
         dcc_object.start()
         dcc_object.stop()
         
    def test_set_speed_with_invalid_parameter(self):
        """ Test that the set_speed function return an error when inavlid parameter is given""" 
        with self.assertRaises(TypeError):
            DCCObject("DCC3",3)
            dcc_object.start()
            DCCObject("DCC3",3).speed = "gas"
            dcc_object.stop()
    
    def test_set_speed_with_valid_parameter(self):
        """ Test that the set_speed function work when a valid parameter is given""" 
        DCCObject("DCC4",4)
        dcc_object.start()
        DCCObject("DCC4",4).speed = 10
        dcc_object.stop()

    def test_f_light_with_valid_parameter(self):
        """Test that the fl function work when a valid parameter is given"""
        DCCObject("DCC4",4)
        dcc_object.start()
        DCCObject("DCC4",4).f_light = True
        dcc_object.stop()
        
    def test_f_light_with_invalid_parameter(self):
        """Test that the fl function return an error when an invalid parameter is given"""
        with self.assertRaises(TypeError):
            DCCObject("DCC4",4)
            dcc_object.start()
            DCCObject("DCC4",4).f_light = "/p "
            dcc_object.stop()
    
    def test_f1_with_invalid_parameter(self):
        """Test that the f1 function return an error when an invalid parameter is given"""
        with self.assertRaises(TypeError):
            DCCObject("DCC4",4)
            dcc_object.start()
            DCCObject("DCC4",4).f1= "hzdlu"
            dcc_object.stop()
        
    
    def test_f1_with_valid_parameter(self):
        """Test that the f1 function work when a valid parameter is given"""
        DCCObject("DCC4",4)
        dcc_object.start()
        DCCObject("DCC4",4).f1= True
        dcc_object.stop()
    
    def test_f2_with_valid_parameter(self):
        """Test that the f2 function work when a valid parameter is given"""
        DCCObject("DCC4",4)
        dcc_object.start()
        DCCObject("DCC4",4).f2= True
        dcc_object.stop()
        
    
    def test_f2_with_invalid_parameter(self):
        """Test that the f2 function return an error when an invalid parameter is given"""
        with self.assertRaises(TypeError):
            DCCObject("DCC4",4)
            dcc_object.start()
            DCCObject("DCC4",4).f2= "jcoe*z^n "
            dcc_object.stop()
            
    def test_f3_with_valid_parameter(self):
        """Test that the f3 function work when a valid parameter is given"""
        DCCObject("DCC4",4)
        dcc_object.start()
        DCCObject("DCC4",4).f3= True
        dcc_object.stop()
        
    
    def test_f3_with_invalid_parameter(self):
        """Test that the f3 function return an error when an invalid parameter is given"""
        with self.assertRaises(TypeError):
            DCCObject("DCC4",4)
            dcc_object.start()
            DCCObject("DCC4",4).f3= "jcoe*z^n "
            dcc_object.stop()
    
    def test_f4_with_valid_parameter(self):
        """Test that the f4 function work when a valid parameter is given"""
        DCCObject("DCC4",4)
        dcc_object.start()
        DCCObject("DCC4",4).f4= True
        dcc_object.stop()
        
    
    def test_f4_with_invalid_parameter(self):
        """Test that the f4 function return an error when an invalid parameter is given"""
        with self.assertRaises(TypeError):
            DCCObject("DCC4",4)
            dcc_object.start()
            DCCObject("DCC4",4).f4= "jcoe*z^n "
            dcc_object.stop()
if __name__ == '__main__':
    unittest.main()

            
 

