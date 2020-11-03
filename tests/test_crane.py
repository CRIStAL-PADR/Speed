# copyright CNRS
#
#
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
        """ Test that the init function works when a correct ip given"""       
        faller.init("172.17.217.217")
    
    def test_change_speed(self):
        """ test that the change_speed function works when given the right ones settings"""  
        faller.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            t = faller.set_speed(motor, 50,n)              
            self.assertEqual(t, 50, n )             
        
    def test_change_speed(self):
        """ test that the change_speed function works when given the right ones settings"""         
        faller.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            t = faller.change_speed(motor, 0)  
            
            self.assertEqual(type(t), int)                  
            t1 = faller.change_speed(motor, 10)
            if t1 == t:
                t2 = faller.change_speed(motor, -20)
                self.assertNotEqual(t,t2)

    def test_change_speed_invalid(self):
        """Test that the change_speed function is returning an exception if an invalid parameters is given""" 
        faller.init("172.17.217.217")
        # Here we test that a string is not considered as a valid parameter
        with self.assertRaises(TypeError):
            t = faller.change_speed("MotorOne", 10)        

        
        with self.assertRaises(RuntimeError):
            t = faller.change_speed(123, 20)        

        # Here we tests that weird values provided as parameter are rejected with an exception
        with self.assertRaises(TypeError):
            for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
                t = faller.change_speed(motor, "20")       

    def test_step(self):
        faller.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            for direction in [faller.MotorDirectionForward, faller.MotorDirectionBackward]:        
                faller.step(motor, direction)        
    
        # Here we test that an out of range motor number rise an exception
    def test_start(self):
        faller.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            for direction in [faller.MotorDirectionForward, faller.MotorDirectionBackward]:        
                faller.start(motor, direction)        

    def test_get_speed_invalid(self):
        """ Test that the get_speed function is returning an exception if an invalid parameters is given"""
        faller.init("172.17.217.217")
        # Here we test that a string is not considered as a valid parameter
        with self.assertRaises(TypeError):
            t = faller.get_speed("xxx", 1) 
        with self.assertRaises(RuntimeError):
            t = faller.get_speed(123, 20)
            
         # Here we test that an out of range crane number rise an exception
        with self.assertRaises(IndexError):
            n > len(ip_master_n)
            
    def test_start_for_invalid(self):
        """ Test that the start_for function is returning an exception if an invalid parameters is given"""
        faller.init("172.17.217.217")
        # Here we test that an int as time rise an exception
        with self.assertRaise(ValueError):
            faller.start_for(5,faller.MotorDirectionForward, 0)
            
        # Here we test that an out of turn rise an exception
        with self.assertRaises(RuntimeError):
            faller.start_for( 5* ureg.second , faller.MotorCrab, -10, 0)
           
        # Here we test that an out of range motor number rise an exception
        with self.assertRaises(RuntimeError):
            faller.start_for(5* ureg.microsecond , -6, faller.MotorDirectionForward,0)  
                  
               
        
        
    def test_startInvalid(self):
        faller.init("172.17.217.217")
        
        # Here we test that an out of range motor number rise an exception
        with self.assertRaises(RuntimeError):
            faller.start(-5, faller.MotorDirectionForward)  
                  
        # Here we test that an out of turn rise an exception
        with self.assertRaises(RuntimeError):
            faller.start(faller.MotorCrab, -10)        

        # Here we tests that weird values provided as parameter are rejected with an exception
        with self.assertRaises(Exception):
            faller.start("Yo", -10) 
        # Here we tests that weird values provided as parameter are rejected with an exception
        with self.assertRaises(RuntimeError):
            faller.start(faller.MotorCrab, "1")        
             
   

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
