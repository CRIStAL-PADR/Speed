import unittest
import requests
import fallerlib

class TestCrane(unittest.TestCase):
    def test_init_with_invalid_ip(self):
        """Test that the init function is returning an exception if an invalid IP is given"""       
        with self.assertRaises(requests.exceptions.ConnectionError):
            fallerlib.init("x6d6q5f4q6fqf")

        with self.assertRaises(requests.exceptions.ConnectTimeout):
            fallerlib.init("172.168.1.1")

    def test_init_with_ip(self):
        """Test that the init function is returning an exception if an invalid IP is given"""       
        fallerlib.init("172.17.217.217")
        
    def test_change_speed(self):
        """Test that the init function is returning an exception if an invalid IP is given"""       
        fallerlib.init("172.17.217.217")
        for motor in [fallerlib.MotorCrab, fallerlib.MotorChassis, fallerlib.MotorSpreader]:
            t = fallerlib.change_speed(motor, 0)  
            
            self.assertEqual(type(t), int)                  
            t1 = fallerlib.change_speed(motor, 10)
            if t1 == t:
                t2 = fallerlib.change_speed(motor, -20)
                self.assertNotEqual(t,t2)

    def test_change_speed_invalid(self):
        fallerlib.init("172.17.217.217")
        # Here we test that a string is not considered as a valid parameter
        with self.assertRaises(TypeError):
            t = fallerlib.change_speed("MotorOne", 10)        

        # Here we test that an out of range motor number rise an exception
        with self.assertRaises(RuntimeError):
            t = fallerlib.change_speed(123, 20)        

        ## Here we tests that weird values provided as parameter are rejected with an exception
        with self.assertRaises(TypeError):
            for motor in [fallerlib.MotorCrab, fallerlib.MotorChassis, fallerlib.MotorSpreader]:
                t = fallerlib.change_speed(motor, "20")        

    def test_start(self):
        fallerlib.init("172.17.217.217")
        for motor in [fallerlib.MotorCrab, fallerlib.MotorChassis, fallerlib.MotorSpreader]:
            for direction in [fallerlib.MotorDirectionForward, fallerlib.MotorDirectionBackward]:        
                fallerlib.start(motor, direction)        

    def test_startInvalid(self):
        fallerlib.init("172.17.217.217")
        with self.assertRaises(RuntimeError):
            fallerlib.start(-5, fallerlib.MotorDirectionForward)        

        with self.assertRaises(RuntimeError):
            fallerlib.start(fallerlib.MotorCrab, -10)        

        with self.assertRaises(Exception):
            fallerlib.start("Yo", -10) 

        with self.assertRaises(RuntimeError):
            fallerlib.start(fallerlib.MotorCrab, "1")        
             
    def test_stop(self):
        fallerlib.init("172.17.217.217")
        for motor in [fallerlib.MotorCrab, fallerlib.MotorChassis, fallerlib.MotorSpreader]:
                fallerlib.stop(motor)        

    def test_stopInvalid(self):
        fallerlib.init("172.17.217.217")
        with self.assertRaises(RuntimeError):
            fallerlib.stop(-5)        

        with self.assertRaises(TypeError):
            fallerlib.stop("Yo") 

    def test_get_battery(self):
        fallerlib.init("172.17.217.217")
        b = fallerlib.get_battery()        
        self.assertEqual(type(b), tuple)
        self.assertEqual(type(b[0]), int)
        
    def test_get_other_esp(self):
        fallerlib.init("172.17.217.217")
        b = fallerlib.get_other_esp("172.17.217.217")        
        self.assertNotEqual(b, None)

if __name__ == '__main__':
    unittest.main()
