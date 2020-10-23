# -*-coding: <Utf-8> -*-
""" Comments for all the librairy """

import requests
import re
import time
crane_number = []

IP_master_n = []
IP_slave_n = []

MotorSpreader = 1
MotorCrab = 2
MotorChassis = 3

MotorDirectionForward = 1
MotorDirectionBackward = -1

# The amount of time to use before the HTTP connection to the board is considered as too long and we thus exit
# by throwing an RuntimeError of type requests.RuntimeErrors.ConnectTimoutRuntimeError. 
timeout = 2.5


def getMotorInfoFromNumber(sNr, n = 0):
    """ Comments about getMotorInfoFromNumber function
    It takes the number of the motor as input and returns the  number with its IP address.
    :param : see def start (sNr, turn) parameters
    
    """
    
    
    IP_master = IP_master_n[n] 
    IP_slave = IP_slave_n[n] 
    
    if not isinstance(sNr, int):
        raise TypeError()
    
    if MotorSpreader == sNr:
        return (IP_slave, 1)
    elif MotorCrab == sNr:
        return (IP_slave, 2)
    elif MotorChassis == sNr:
        return (IP_master, 1)
        
    raise RuntimeError("Invalid motor number, must be MotorSpreader, MotorCrab or MotorChassis, got "+str(sNr))
    
    
def step(sNr,turn,n=0):
    """ Comments about the step function
        :param sNr: This is the first of the arguments. It indicates the engine number that we would like to start. It takes the values ​​1 2 3 which indicates motors 1 2 and 3 respectively
        :param turn: It indicates the direction in which we would like to run the engine. 1 for moving forward and -1 for moving backward.

    Example:
        start(MotorSpreader, MotorDirectionBackward)  turns the spreader backwards
    """
    start(sNr, turn, n = 0)


    
    
# Démarer grueB, motor2, turn=-1       
def start(sNr, turn, n = 0):
    """ Comments about the start function
        :param sNr: This is the first of the arguments. It indicates the engine number that we would like to start. It takes the values ​​1 2 3 which indicates motors 1 2 and 3 respectively
        :param turn: It indicates the direction in which we would like to run the engine. 1 for moving forward and -1 for moving backward.

    Example:
        craneGauche = fallerlib.init("172.168.1.0") ## craneA = 0 
        craneDroite = fallerlib.init("172.167.2.0") ## craneB = 1
        
        fallerlib.start(craneGauche, MotorChassis, Forward) 
        fallerlib.start(craneDroit, MotorChassis, Forward)
        fallerlib.start(craneGauche, MotorCrub, Forward) 

    """
    global timeout
           
    if turn not in [MotorDirectionForward, MotorDirectionBackward]:
        raise RuntimeError("Invalid parameter, turn must be either MotorDirectionForward or MotorDirectionBackward. Got " +str(turn))			
    
    ip, numMotor = getMotorInfoFromNumber( sNr, n=0)
    r = requests.get("http://"+ip+"/startM?sNr="+str(numMotor)+"&turn="+str(turn),timeout=timeout)
 
    if r.status_code !=200:
        raise RuntimeError("Unable to control the motor, "+str(r.status_code))

    if r.text != "ok":
        raise RuntimeError("Able to controle the motor but got not OK answer: "+r.text)
        
        
def set_speed(sNr, speed, n = 0):
    """ set the speed for a motor """    		
    current = change_speed(n,sNr, 0) 
    diff = speed - current 
    return change_speed(sNr, diff , n=0)    

def get_speed(sNr, n=0):
    """ Returns the current speed for a motor """    		
    return change_speed(sNr, 0 , n = 0)



def change_speed(sNr, diff, n=0):
    global IP_master, IP_slave, timeout
    """ Comments about changePWM function
	This function allows us to modify the engine speed while varying its cyclic ratio. 
	
       :param sNr:  see def start (sNr, turn) parameters
       :param diff: This parameter is used to vary the speed of the motor. It takes the values between 0 and 100 for the acceleration and 0 and -70 for the slowdown.
       It should be noted that the maximum speed that the motor can reach is 100.
	   
     Example:
		changePWMM(3, -60) : allows to decrease the motor speed 3 by 60
		
     """
    ip, numMotor = getMotorInfoFromNumber(sNr, n = 0)
    r = requests.get("http://"+ip+"/changePWMTV?sNr="+str(numMotor)+"&diff="+str(diff), timeout=timeout)
    
    if r.status_code != 200: 
        raise RuntimeError("Unable to change the speed of the motor,"+str(r.status_code))
    
    result = re.search("neuer Speed=\s+(\d+)", r.text)
    num = int(result.groups()[0])
    return num





def get_battery(n=0):
    global IP_master_n, IP_slave_n, timeout

    IP_master = IP_master_n[n] 
    IP_slave = IP_slave_n[n] 

    r1=requests.get("http://"+IP_master+"/getBat?n=1", timeout=timeout)
    r2=requests.get("http://"+IP_slave+"/getBat?n=2", timeout=timeout)

    if r1.status_code != 200: 
        raise RuntimeError("Please check if the r1 battery is correctly powered")
    
    if r2.status_code != 200: 
        raise RuntimeError("Please check if the r2 battery is correctly powered")
    
    return (int(r1.text), int(r2.text))
   
    
def init(ip):
    """ 
    The purpose of this function is to initialize the IP address of the master and once the IP address of the master is
    initialized to obtain that of the slave thanks to the getOtherEsp function   
    
    Example:
        craneA = fallerlib.init("172.168.1.0") # len(IP_masster_n)-1 = 0 
        craneD = fallerlib.init("172.167.2.0")
        craneE = fallerlib.init("215.1.2.0")
    
        fallerlib.start(craneA, MotorChassis, Forward) 
        fallerlib.start(craneB, MotorChassis, Forward) 
    """

    global IP_master_n, IP_slave_n
    IP_master_n.append(ip) 
    IP_slave_n.append( get_other_esp(ip) )
    crane_number.append(len(IP_master_n)-1)
 
    return len(IP_master_n)-1   
    
    
    

    
def get_other_esp(ip):
    """ Comments about changePWM function
	This function has the role of launching a request to obtain the IP address of the slave
    """
    global timeout
    r = requests.get("http://" + ip + "/getOtherEsp", timeout = timeout)
    if r.status_code != 200:
        raise RuntimeError ("I failed to get the IP address of the slave. Check if the latter is correctly supplied then try again")

    return r.text 

	
if __name__ == "__main__":
    ip = "172.17.217.217"
    
    init(ip)
    print(crane_number[0])
    
    init(ip)
    print(crane_number[1])
    #step(MotorSpreader, MotorDirectionBackward,2)

    print(crane_number)
    
  
    
