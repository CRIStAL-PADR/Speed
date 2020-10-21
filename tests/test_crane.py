import unittest
import requests
from speedlib.cranes import faller

class TestCrane(unittest.TestCase):
    def test_init_with_invalid_ip(self):
        """Test that the init function is returning an exception if an invalid IP is given"""       
        with self.assertRaises(requests.exceptions.ConnectionError):
            faller.init("x6d6q5f4q6fqf")

        with self.assertRaises(requests.exceptions.ConnectTimeout):
            faller.init("172.168.1.1")

    def test_init_with_ip(self):
        """Test that the init function is returning an exception if an invalid IP is given"""       
        faller.init("172.17.217.217")
    
    def test_change_speed(self):
        faller.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            t = faller.set_speed(motor, 50)              
            self.assertEqual(t, 50)             
        
    def test_change_speed(self):
        """Test that the init function is returning an exception if an invalid IP is given"""       
        faller.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            t = faller.change_speed(motor, 0)  
            
            self.assertEqual(type(t), int)                  
            t1 = faller.change_speed(motor, 10)
            if t1 == t:
                t2 = faller.change_speed(motor, -20)
                self.assertNotEqual(t,t2)

    def test_change_speed_invalid(self):
        faller.init("172.17.217.217")
        # Here we test that a string is not considered as a valid parameter
        with self.assertRaises(TypeError):
            t = faller.change_speed("MotorOne", 10)        

        # Here we test that an out of range motor number rise an exception
        with self.assertRaises(RuntimeError):
            t = faller.change_speed(123, 20)        

        ## Here we tests that weird values provided as parameter are rejected with an exception
        with self.assertRaises(TypeError):
            for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
                t = faller.change_speed(motor, "20")        

    def test_step(self):
        faller.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            for direction in [faller.MotorDirectionForward, faller.MotorDirectionBackward]:        
                faller.step(motor, direction)        


    def test_start(self):
        faller.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            for direction in [faller.MotorDirectionForward, faller.MotorDirectionBackward]:        
                faller.start(motor, direction)        

    def test_startInvalid(self):
        faller.init("172.17.217.217")
        with self.assertRaises(RuntimeError):
            faller.start(-5, faller.MotorDirectionForward)        

        with self.assertRaises(RuntimeError):
            faller.start(faller.MotorCrab, -10)        

        with self.assertRaises(Exception):
            faller.start("Yo", -10) 

        with self.assertRaises(RuntimeError):
            faller.start(faller.MotorCrab, "1")        
             
    def test_stop(self):
        faller.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
                faller.stop(motor)        

    def test_stopInvalid(self):
        faller.init("172.17.217.217")
        with self.assertRaises(RuntimeError):
            faller.stop(-5)        

        with self.assertRaises(TypeError):
            faller.stop("Yo") 

    def test_get_battery(self):
        faller.init("172.17.217.217")
        b = faller.get_battery()        
        self.assertEqual(type(b), tuple)
        self.assertEqual(type(b[0]), int)
        
    def test_get_other_esp(self):
        faller.init("172.17.217.217")
        b = faller.get_other_esp("172.17.217.217")        
        self.assertNotEqual(b, None)

if __name__ == '__main__':
    unittest.main()
