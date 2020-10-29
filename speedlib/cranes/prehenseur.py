from pint import UnitRegistry

def gripper( n=0 ):
    global timeout
    """  It is a function to control the gripper
        : param : x is the parameter which allows to activate or not the magnet. 
         This sensor has as output d which is the distance which separates it from an obstacle (I take here the ceiling of the container)
        :param d :  it gives a certain value that we can read
        
        :n  this is the number of the crane
    """

    d = sensor (n) * ureg.meter
    x = False # initial state value (convention)
    if d > 0.002 *ureg.meter : #for exemple
        x = False # The magnet is disabled
    if d < 0.002 * ureg.meter : # for exemple
        x = True # The magnet is disabled
    ip, numMotor = get_motor_info_from_number(2, n)
    
    r = requests.get("http://"+ip+"/gripper?sNr="+str(numMotor)+"&x="+str(x),timeout=timeout)
    
"""
We can imagine a function which takes as input the number of the crane and therefore the sensor which will be placed on the drue and which will return
a certain distance d that we will recover in the seize function
"""

def sensor(n = 0):
    return d
