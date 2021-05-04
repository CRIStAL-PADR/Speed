import unittest
from speedlib.dcc import dcc_object, dcc_trains



class TestTrain(unittest.TestCase):
    dcc_object.start()
    def test_init_with_invalid_adress(self):
        """Check that init returns an error when entering an invalid parameter"""
        
        with self.assertRaises(TypeError):
            dcc_trains.Train("DCC1", "ad")
    def test_init_with_invalid_name(self):
        """Check that init returns an error when entering an invalid parameter"""
        with self.assertRaises(TypeError):
            dcc_trains.Train(41, 5)
    def test_init_with_valid_adress_name(self):
         """ Test that the init function works when a correct adress and name are  given""" 
         dcc_trains.Train("DCC4", 4)
    def test_set_speed_with_invalid_parameter(self):
        """ Test that the set_speed function return an error when inavlid parameter is given""" 
        with self.assertRaises(TypeError):
            dcc_trains.Train("DCC3",3).speed = "gas"
    
    def test_set_speed_with_valid_parameter(self):
        """ Test that the set_speed function work when a valid parameter is given""" 
        dcc_trains.Train("DCC6",6).speed = 10
    
    
    def test_f_light_with_valid_parameter(self):
        """Test that the fl function work when a valid parameter is given"""
        dcc_trains.Train("DCC4",4).fl = True
        
    def test_f_light_with_invalid_parameter(self):
        """Test that the fl function return an error when an invalid parameter is given"""
        with self.assertRaises(TypeError):
            dcc_trains.Train("DCC4",4).f_light = 5.6
    
    
    def test_f1_with_invalid_parameter(self):
        """Test that the f1 function return an error when an invalid parameter is given"""
        with self.assertRaises(TypeError):
            dcc_trains.Train("DCC4",4).f1= "hzdlu"
        
    
    def test_f1_with_valid_parameter(self):
        """Test that the f1 function work when a valid parameter is given"""
        dcc_trains.Train("DCC4",4).f1 = False

    def test_f2_with_valid_parameter(self):
        """Test that the f2 function work when a valid parameter is given"""
        dcc_trains.Train("DCC4",4).f2 = False
        
    
    def test_f2_with_invalid_parameter(self):
        """Test that the f2 function return an error when an invalid parameter is given"""
        with self.assertRaises(TypeError):
            dcc_trains.Train("DCC4",4).f2 = 6
    
    def test_f3_with_invalid_parameter(self):
        """Test that the f3 function return an error when an invalid parameter is given"""
        with self.assertRaises(TypeError):
            dcc_trains.Train("DCC8",8).f2= " /"
    

    dcc_object.stop()
    

if __name__ == '__main__':
    unittest.main()
            
 
