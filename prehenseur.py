from pint import UnitRegistry

def gripper(sNr, x = 1 , n=0 ):
    global timeout
    """  It is a function to control the gripper
        : param :  sNr This is the motor on which the magnet will be. It must be 2 because the magnet will be on the motorCrab
        : param : x is the parameter which allows to activate or not the magnet. 
            We will take the values ​​1 to activate and 0 to switch off
         This sensor has as output d which is the distance which separates it from an obstacle (I take here the ceiling of the container)
        :param d :  it gives a certain value that we can read
        
        :n  this is the number of the crane
    """

    d = sensor (n) * ureg.meter
    x = 1 # initial state value (convention)
    if sNr !=2 :
        raise ValueError (" The expected value is 2 but  got ".format(sNr))
    if x !=0 or x!=1 : 
        raise ValueError ("The value must be  0 soit 1 but got ".format(x))
    if not isinstance(x, int) :
        raise TypeError("x must be integer type")
    if d > 0.002 *ureg.meter : #for exemple
        x = 0 # he magnet is disabled
    if d < 0.002 * ureg.meter : # for exemple
        x = 1 #he magnet is disabled
    ip, numMotor = get_motor_info_from_number(sNr, n)
    
    r = requests.get("http://"+ip+"/gripper?sNr="+str(numMotor)+"&x="+str(x),timeout=timeout)
    
"""
We can imagine a function which takes as input the number of the crane and therefore the sensor which will be placed on the drue and which will return
a certain distance d that we will recover in the seize function
"""

def sensor(n = 0):
    return d
