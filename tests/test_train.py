import unittest
from speedlib.trains import dcc
from speedlib.trains.dcc import Train

train = Train()

class TestTrain(unittest.TestCase):
    def test_init_with_invalid_adress(self):
        """Check that init returns an error when entering an invalid parameter"""
        with self.assertRaises(RuntimeError):
            train.init("15poiu", 0)
            
        with self.assertRaises(RuntimeError):
            train.init("DCC1", 128)
            
        with self.assertRaises(TypeError):
            train.init("DCC1", "ad")
            
    def test_init_with_invalid_name(self):
        """Check that init returns an error when entering an invalid parameter"""
        with self.assertRaises(TypeError):
            train.init(41, 5)
            
    def test_init_with_valid_adress_name(self):
         """ Test that the init function works when a correct adress and name are  given""" 
         train.init("DCC3", 3)
         
    def test_set_speed_with_invalid_parameter(self):
        """ Test that the set_speed function return an error when inavlid parameter is given""" 
        train.init("DCC3",3)
        dcc.start()
        train.speed = "gas"
    
    def test_set_speed_with_valid_parameter(self):
        """ Test that the set_speed function work when a valid parameter is given""" 
        train.init("DCC3",3)
        dcc.start()
        train.speed = 10
        

if __name__ == '__main__':
    unittest.main()
            
 