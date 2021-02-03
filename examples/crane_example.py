# -*-coding: <Utf-8> -*-
"""
 Here is an example of how to use the faller library and the functions that we can perform with it  
"""
from speedlib.cranes import faller
from speedlib.cranes.faller import Crane

# Initialization of the board using its ip address.
# In case of error exception are risen. 
ip_1 = "172.17.217.217"
ip_2 = "172.17.217.217"
crane_1 = Crane()
crane_2 = Crane()
crane_1.init(ip_1)
crane_2.init(ip_2)

# To move the Crab, SPreader or Chassi on step you can do
# See help (Crane().step) for more information on the parameters that this function takes
crane_2.step(faller.MotorChassis ,faller.MotorDirectionBackward)
crane_1.step(faller.MotorCrab ,faller.MotorDirectionForward)

# To move the MotorChassis for 5 milliseconds you can do
crane_2.start_for(20*faller.ureg.millisecond,faller.MotorChassis,faller.MotorDirectionForward)

# To get the battery state you can use get_battery function. It returns a tuple of each battery detected on the board. 
print(crane_1.battery)

# Each motor can be configured to operate at a specific speed. To retrieve the configured speed you use the get_speed function. 
print(crane_2.get_speed(faller.MotorCrab))

#We can also change the speed in order to set a new one
print(crane_1.change_speed(faller.MotorCrab, -40))

