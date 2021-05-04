import unittest
from speedlib.dcc import dcc_object, dcc_switches

class TestSwitch(unittest.TestCase):
    dcc_object.start()
    def test_init_with_invalid_adress(self):
        """Check that init returns an error when entering an invalid parameter"""
        with self.assertRaises(TypeError):
            dcc_switches.Switch("DCC1", "ad")
            
    def test_init_with_invalid_name(self):
        """Check that init returns an error when entering an invalid parameter"""
        with self.assertRaises(TypeError):
            dcc_switches.Switch(41, 5)
            
    def test_init_with_adress_out_of_range(self):
        """Check that init returns an error when entering an invalid parameter"""
        with self.assertRaises(RuntimeError):
            dcc_switches.Switch("DCC5", 5)
            
    def test_init_with_valid_adress_name(self):
         """ Test that the init function works when a correct adress and name are  given""" 
         dcc_switches.Switch("DCC4", 120)
         
    def test_biais_with_valid_parameter(self):
        """Test that the fl function work when a valid parameter is given"""
        dcc_switches.Switch("DCC4", 120).biais = True
        
    def test_biais_with_valid_parameter(self):
        """Test that the fl function return an error when an invalid parameter is given"""
        with self.assertRaises(TypeError):
            dcc_switches.Switch("DCC4", 120).biais = "j zxa"
    dcc_object.stop()