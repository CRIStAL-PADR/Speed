import unittest
import requests
import fallerlib

class TestCrane(unittest.TestCase):
    def test_initWithInvalidIP(self):
        """Test that the init function is returning an exception if an invalid IP is given"""       
        with self.assertRaises(requests.exceptions.ConnectionError):
            fallerlib.init("x6d6q5f4q6fqf")

        with self.assertRaises(requests.exceptions.ConnectTimeout):
            fallerlib.init("172.168.1.1")

    def test_initWithIP(self):
        """Test that the init function is returning an exception if an invalid IP is given"""       
        fallerlib.init("172.17.217.217")
        self.assertNotEqual(t, None)        

    def test_change_speed(self):
        """Test that the init function is returning an exception if an invalid IP is given"""       
        fallerlib.init("172.17.217.217")
        for motor in [fallerlib.MotorCrab, fallerlib.MotorChassis, fallerlib.MotorSpreader]:
            t = fallerlib.change_speed(fallerlib.MotorCrab)        
            t1 = fallerlib.change_speed(10)
            if t1 == t:
                t2 = fallerlib.change_speed(-20)
                self.assertNotEqual(t,t2)

    def test_change_speedInvalid(self):
        fallerlib.init("172.17.217.217")
        # Here we test that a string is not considered as a valid parameter
        with self.assertRaises(TypeError):
            t = fallerlib.change_speed("MotorOne", 10)        

        # Here we test that an out of range motor number rise an exception
        with self.assertRaises(TypeError):
            t = fallerlib.change_speed(123, 20)        

        ## Here we tests that weird values provided as parameter are rejected with an exception
        with self.assertRaises(TypeError):
            for motor in [fallerlib.MotorCrab, fallerlib.MotorChassis, fallerlib.MotorSpreader]:
                t = fallerlib.change_speed(motor, "20")        

    def test_start(self):
        fallerlib.init("172.17.217.217")
        for motor in [fallerlib.MotorCrab, fallerlib.MotorChassis, fallerlib.MotorSpreader]:
            t = fallerlib.start(motor)        
            
    def test_stop(self):
        fallerlib.init("172.17.217.217")
        for motor in [fallerlib.MotorCrab, fallerlib.MotorChassis, fallerlib.MotorSpreader]:
            t = fallerlib.stop(motor)        

    def test_get_battery(self):
        fallerlib.init("172.17.217.217")
        b = fallerlib.get_battery(motor)        
        fallerlib.assertEqual(type(b), tuple)

    def test_get_other_esp(self):
        fallerlib.init("172.17.217.217")
        b = fallerlib.get_other_esp("172.17.217.217")        
        fallerlib.assertEqual(type(b), tuple)

if __name__ == '__main__':
    unittest.main()
