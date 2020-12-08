# -*-coding: <Utf-8> -*-
""" Comments for all the librairy """

import requests
import re
import time
import asyncio
from pint import UnitRegistry

timeout = 2.5

class Faller:
    
    def __init__(self):
        
        self.ureg = UnitRegistry()
        self.MotorSpreader = 1
        self.MotorCrab = 2
        self.MotorChassis = 3
        self.MotorDirectionBackward = 1
        self.MotorDirectionForward = 2
        
        


    def get_motor_info_from_number(self, sNr):
        
        
        
        if not isinstance(sNr, int):
            raise TypeError(" The value of n must be an integer but got " +str(sNr))
        
    
    
        if self.MotorSpreader == sNr:
            return (self.ip_slave, 1)
        elif self.MotorCrab == sNr:
            return (self.ip_slave, 2)
        elif self.MotorChassis == sNr:
            return (self.ip_master, 1)
        
        raise RuntimeError("Invalid motor number, must be MotorSpreader, MotorCrab or MotorChassis, got "+str(sNr))

    def start (self, sNr, turn):
    

      
           
        if turn not in [self.MotorDirectionForward, self.MotorDirectionBackward]:
            raise RuntimeError("Invalid parameter, turn must be either MotorDirectionForward or MotorDirectionBackward. Got " +str(turn))			
    
        ip, numMotor = self.get_motor_info_from_number(sNr)
        r = requests.get("http://"+ip+"/startM?sNr="+str(numMotor)+"&turn="+str(turn),timeout=timeout)
 
        if r.status_code !=200:
            raise RuntimeError("Unable to control the motor, "+str(r.status_code))

        if r.text != "ok":
            raise RuntimeError("Able to controle the motor but got not OK answer: "+r.text)
        return r.text
        
    def step (self, sNr, turn):
        
        return self.start(sNr, turn)
  
    def get_battery(self):
    
        timeout

        r1=requests.get("http://"+self.ip_master+"/getBat?n=1", timeout=timeout)
        r2=requests.get("http://"+self.ip_slave+"/getBat?n=2", timeout=timeout)

        if r1.status_code != 200: 
            raise RuntimeError("Please check if the r1 battery is correctly powered")
    
        if r2.status_code != 200: 
            raise RuntimeError("Please check if the r2 battery is correctly powered")
    
        return (int(r1.text), int(r2.text))

    def change_speed(self, sNr, diff):
 
        timeout 
		
    
        if not isinstance (diff, int):
            raise TypeError()
        
        ip, numMotor = self.get_motor_info_from_number(sNr)
        r = requests.get("http://"+ip+"/changePWMTV?sNr="+str(numMotor)+"&diff="+str(diff), timeout=timeout)
    
        if r.status_code != 200: 
            raise RuntimeError("Unable to change the speed of the motor,"+str(r.status_code))
    
        result = re.search("neuer Speed=\s+(\d+)", r.text)
        num = int(result.groups()[0])
        return num


    def init (self, ip):
        self.ip_master = ip
        self.ip_slave = self.get_other_esp(ip) 
    
 

    def get_other_esp(self, ip):
   
        global timeout
        r = requests.get("http://" + ip + "/getOtherEsp", timeout = timeout)
        if r.status_code != 200:
            raise RuntimeError ("I failed to get the IP address of the slave. Check if the latter is correctly supplied then try again")
        return r.text
        



        

if __name__ == "__main__":
    
   
    ip_1 = "172.17.217.217"
    ip_2 = "172.17.217.217"
    
    crane_1 = Faller()
    crane_1.init(ip_1)
    print(crane_1.get_battery())
    print(crane_1.change_speed(crane_1.MotorChassis,-50))
    
    crane_2 = Faller()
    crane_2.init(ip_2)
    print(crane_2.get_battery())
    print(crane_1.change_speed(crane_2.MotorCrab,-20))
    crane_2.step(crane_2.MotorChassis , crane_2.MotorDirectionBackward)
    crane_1.step(crane_1.MotorCrab, crane_1.MotorDirectionBackward)
