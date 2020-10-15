# -*-coding: <Utf-8> -*-
""" Comments for all the librairy """

import requests
import re

IP_master= "172.17.217.217"
IP_slave= "172.17.217.61"

MotorSpreader = 1
MotorCrab = 2
MotorChassis = 3

MotorDirectionForward = 1
MotorDirectionBackward = -1

# The amount of time to use before the HTTP connection to the board is considered as too long and we thus exit
# by throwing an RuntimeError of type requests.RuntimeErrors.ConnectTimoutRuntimeError. 
timeout = 1.0

def getMotorInfoFromNumber(sNr):
    """ Comments about getMotorInfoFromNumber function
    It takes the number of the motor as input and returns the  number with its IP address.
    :param : see def start (sNr, turn) parameters
    
    """
    global IP_master, IP_slave 
    
    if not isinstance(sNr, int):
        raise TypeError()
    
    if MotorSpreader == sNr:
        return (IP_slave, 1)
    elif MotorCrab == sNr:
        return (IP_slave, 2)
    elif MotorChassis == sNr:
        return (IP_master, 1)
        
    raise RuntimeError("Invalid motor number, must be MotorSpreader, MotorCrab or MotorChassis, got "+str(sNr))


def step(sNr,turn):
    """ Comments about the start function
        :param sNr: This is the first of the arguments. It indicates the engine number that we would like to start. It takes the values ​​1 2 3 which indicates motors 1 2 and 3 respectively
        :param turn: It indicates the direction in which we would like to run the engine. 1 for moving forward and -1 for moving backward.

    Example:
        start(MotorSpreader, MotorDirectionBackward)  turns the spreader backwards
    """
    start(sNr, turn)

def start(sNr,turn):
    """ Comments about the start function
        :param sNr: This is the first of the arguments. It indicates the engine number that we would like to start. It takes the values ​​1 2 3 which indicates motors 1 2 and 3 respectively
        :param turn: It indicates the direction in which we would like to run the engine. 1 for moving forward and -1 for moving backward.

    Example:
        start(MotorSpreader, MotorDirectionBackward)  turns the spreader backwards
    """
    global IP_master, IP_slave, timeout
            
    if turn not in [MotorDirectionForward, MotorDirectionBackward]:
        raise RuntimeError("Invalid parameter, turn must be either MotorDirectionForward or MotorDirectionBackward. Got " +str(turn))			
    
    ip, numMotor = getMotorInfoFromNumber(sNr)
    r = requests.get("http://"+ip+"/startM?sNr="+str(numMotor)+"&turn="+str(turn),timeout=timeout)
 
    if r.status_code !=200:
        raise RuntimeError("Unable to control the motor, "+str(r.status_code))

    if r.text != "ok":
        raise RuntimeError("Able to controle the motor but got not OK answer: "+r.text)
        

def stop(sNr):
    """ Comments about the stopfunction
        see def start (sNr, turn) parameters
    """
    global IP_master, IP_slave, timeout
    
    ip, numMotor = getMotorInfoFromNumber(sNr)
    r= requests.get("http://"+ip+"/stopM?sNr="+str(numMotor), timeout=timeout)
    print(r.text)
    if r.text != "ok":
        raise RuntimeError("Able to controle the motor bur got not ok answer:"+r.text)
    if r.status_code !=200:
        raise RuntimeError("Unable to stop the motor,"+str(r.status_code) )


def set_speed(sNr, speed):
    current = change_speed(sNr, 0) 
    diff = speed-current           
    return change_speed(sNr, diff)   

def change_speed(sNr, diff):
    global IP_master, IP_slave, timeout
    """ Comments about changePWM function
	This function allows us to modify the engine speed while varying its cyclic ratio. il prend en paraamètre sNr et diff
	
       :param sNr:  see def start (sNr, turn) parameters
       :param diff: This parameter is used to vary the speed of the motor. It takes the values 5 between 0 and 100 for the acceleration and 0 and -100 for the slowdown.
       It should be noted that the maximum speed that the motor can reach is 100.
	   
     Example:
		changePWMM(3, -60) : allows to decrease the motor speed 3 by 60
		
     """
    ip, numMotor = getMotorInfoFromNumber(sNr)
    if diff < -70 or diff > 100:
        raise RuntimeError("Invalide parameter !!!! diff must be between -70 and 100:"+str(diff))
    
    r = requests.get("http://"+ip+"/changePWMTV?sNr="+str(numMotor)+"&diff="+str(diff), timeout=timeout)
    
    if r.status_code != 200: 
        raise RuntimeError("Unable to change the speed of the motor,"+str(r.status_code))
    
    result = re.search("neuer Speed=\s+(\d+)", r.text)
    num = int(result.groups()[0])
    return num
    

def get_battery():
    global IP_master, IP_slave, timeout
    
    r1=requests.get("http://"+IP_master+"/getBat?n=1", timeout=timeout)
    r2=requests.get("http://"+IP_slave+"/getBat?n=2", timeout=timeout)

    if r1.status_code != 200: 
        raise RuntimeError("Please check if the r1 battery is correctly powered")
    
    if r2.status_code != 200: 
        raise RuntimeError("Please check if the r2 battery is correctly powered")
    
    return (int(r1.text), int(r2.text))
    
def init(IP):
    """ Comments about changePWM function
The purpose of this function is to initialize the IP address of the master and once the IP address of the master is
 initialized to obtain that of the slave thanks to the getOtherEsp function   
    
    
    """
    global IP_master, IP_slave
    IP_master= IP
    IP_slave = get_other_esp(IP)
    
def get_other_esp(IP):
    """ Comments about changePWM function
	This function has the role of launching a request to obtain the IP address of the slave
    """
    global timeout
    r = requests.get("http://" + IP +"/getOtherEsp", timeout=timeout)
    if r.status_code != 200:
        raise RuntimeError ("I failed to get the IP address of the slave. Check if the latter is correctly supplied then try again")

    return r.text 

	
