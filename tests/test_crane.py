"""
    Copyright (C) 2021  CNRS
    This file is part of "Speedlib".
    "Speedlib" is an API built for the use case of autonomous navigation.
    It has  been developed to control quay cranes and trains of multimodal
    waterborne Lab as part of The SPEED project, a project which aims to
    enhance and support the growth of a system of connected port solutions,
    with the use of data science and IoT (Internet of Things) technologies.
    The library allows controlling the motion of the IoT devices at H0 scale
    in automatic mode, in three directions and exchanging with the information
    system for overall management
"""
import unittest
import requests
from speedlib.cranes import faller
crane = faller.Crane()
class TestCrane(unittest.TestCase):
    def test_init_with_invalid_ip(self):
        """Test that the init function is returning an exception if an invalid IP is given"""
        with self.assertRaises(requests.exceptions.ConnectionError):
            crane.init("x6d6q5f4q6fqf")

        with self.assertRaises(requests.exceptions.ConnectTimeout):
            crane.init("172.168.1.1")
    def test_init_with_ip(self):
        """ Test that the init function works when a correct ip given"""
        crane.init("172.17.217.217")

    def test_get_other_esp(self):
        """ Test that the _get_other_esp function works when a correct ip given"""
        crane.init("172.17.217.217")
        b = crane.get_other_esp("172.17.217.217")
        self.assertNotEqual(b, None)

    def test_change_speed(self):
        """ test that the change_speed function works when given the right ones settings"""
        crane.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            t = crane.set_speed(motor, 50)
            self.assertEqual(t, 50 )

    def test_change_speed(self):
        """ test that the change_speed function works when given the right ones settings"""
        crane.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            t = crane.change_speed(motor, 0)

            self.assertEqual(type(t), int)
            t1 = crane.change_speed(motor, 10)
            if t1 == t:
                t2 = crane.change_speed(motor, -20)
                self.assertNotEqual(t,t2)

    def test_change_speed_invalid(self):
        """Test that the change_speed function is returning an exception if an invalid parameters is given"""
        crane.init("172.17.217.217")
        # Here we test that a string is not considered as a valid parameter
        with self.assertRaises(TypeError):
            t = crane.change_speed("MotorOne", 10)

        with self.assertRaises(RuntimeError):
            t = crane.change_speed(123, 20)

        # Here we tests that weird values provided as parameter are rejected with an exception
        with self.assertRaises(TypeError):
            for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
                t = crane.change_speed(motor, "20")

    def test_step(self):
        """ test that the set_speed function works when given the right ones settings"""
        crane.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            for direction in [faller.MotorDirectionForward, faller.MotorDirectionBackward]:
                crane.step(motor, direction)

    def test_start(self):
        """ test that the start function works when given the right ones settings"""
        crane.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
            for direction in [faller.MotorDirectionForward, faller.MotorDirectionForward]:
                crane.start(motor, direction)

    def test_stop(self):
        """ test that the stop function works when given the right ones settings"""
        crane.init("172.17.217.217")
        for motor in [faller.MotorCrab, faller.MotorChassis, faller.MotorSpreader]:
                crane.stop(motor)

    def test_get_speed_invalid(self):
        """ Test that the get_speed function is returning an exception if an invalid parameters is given"""
        crane.init("172.17.217.217")
        # Here we test that a string is not considered as a valid parameter
        with self.assertRaises(TypeError):
            t = crane.get_speed("xxx")
        with self.assertRaises(RuntimeError):
            t = crane.get_speed(123)

    def test_start_for_invalid(self):
        """ Test that the start_for function is returning an exception if an invalid parameters is given"""
        crane.init("172.17.217.217")
        # Here we test that an int as time rise an exception
        with self.assertRaises(ValueError):
            crane.start_for(5,faller.MotorSpreader, faller.MotorDirectionBackward)

        # Here we test that an out of turn rise an exception
        with self.assertRaises(RuntimeError):
            crane.start_for( 5* faller.ureg.second , faller.MotorCrab, -10)

        # Here we test that an out of range motor number rise an exception
        with self.assertRaises(RuntimeError):
            crane.start_for(5* faller.ureg.microsecond , -6, faller.MotorDirectionForward)


    def test_start_invalid(self):
        """ Test that the start function is returning an exception if an invalid parameters is given"""
        crane.init("172.17.217.217")

        # Here we test that an out of range motor number rise an exception
        with self.assertRaises(RuntimeError):
            crane.start(-5, faller.MotorDirectionForward)

        # Here we test that an out of turn rise an exception
        with self.assertRaises(RuntimeError):
            crane.start(faller.MotorCrab, -10)

        # Here we tests that weird values provided as parameter are rejected with an exception
        with self.assertRaises(Exception):
            crane.start("Yo", -10)
        # Here we tests that weird values provided as parameter are rejected with an exception
        with self.assertRaises(RuntimeError):
            crane.start(faller.MotorCrab, "1")

    def test_get_battery(self):
        """ test that the _get_battery function works when given the right ones settings"""
        crane.init("172.17.217.217")
        b = crane._get_battery()
        self.assertEqual(type(b), tuple)
        self.assertEqual(type(b[0]), int)






if __name__ == '__main__':
    unittest.main()
