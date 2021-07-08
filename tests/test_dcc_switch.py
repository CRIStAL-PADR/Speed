import unittest
from speedlib.dcc import dcc_object, dcc_switches

class TestSwitch(unittest.TestCase):
    dcc_object.start()
    def test_init_with_invalid_adress(self):
        """Check that init returns an error when entering an invalid parameter"""
        with self.assertRaises(TypeError):
            dcc_switches.Switch("DCC1", "ad", 1)
            
    def test_init_with_invalid_name(self):
        """Check that init returns an error when entering an invalid parameter"""
        with self.assertRaises(TypeError):
            dcc_switches.Switch(41, 5, 2)
    
    def test_init_with_invalid_biais_id(self):
        """Check that init returns an error when entering an invalid parameter"""
        with self.assertRaises(TypeError):
            dcc_switches.Switch("DCC3", "3", "c")
    
    def test_init_with_invalid_biais_id(self):
        """Check that init returns an error when entering an invalid parameter"""
        with self.assertRaises(ValueError):
            dcc_switches.Switch("DCC3", "3", 5)
        
            
    #def test_init_with_adress_out_of_range(self):
        #"""Check that init returns an error when entering an invalid parameter"""
        #with self.assertRaises(RuntimeError):
            #dcc_switches.Switch("DCC5", 5)
            
    def test_init_with_valid_adress_parameters(self):
         """ Test that the init function works when a correct adress name and biais_id are  given""" 
         dcc_switches.Switch("DCC3", 3, 1)
         
    def test_biais_with_valid_parameter(self):
        """Test that the fl function work when a valid parameter is given"""
        dcc_switches.Switch("DCC3", 3, 2).biais = True
        
    def test_biais_with_invalid_state_parameter(self):
        """Test that the fl function return an error when an invalid parameter is given"""
        with self.assertRaises(TypeError):
            dcc_switches.Switch("DCC3", 3, 2).biais = "j zxa"
    dcc_object.stop()