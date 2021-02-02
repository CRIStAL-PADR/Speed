# -*-coding: <Utf-8> -*-
"""
 Here is an example of how to use the faller library and the functions that we can perform with it  
"""
from speedlib.cranes import faller
import time
 
# Initialization of the board using its ip address.
# In case of error exception are risen. 
faller.init("172.17.217.217")

# To move the Crab, SPreader or Chassi on step you can do
# See help (faller.stept) for more information on the parameters that this function takes
faller.step(faller.MotorSpreader, faller.MotorDirectionForward)
faller.step(faller.MotorCrab, faller.MotorDirectionBackward)
faller.step(faller.MotorChassis, faller.MotorDirectionForward)

# To move the MotorCrab for 5 seconds you can do
init_time = time.time()
while (time.time() -init_time ) < 5.0:
    faller.step(faller.MotorCrab, faller.MotorDirectionBackward)  

# To get the battery state you can use get_battery function. It returns a tuple of each battery detected on the board. 
levels = faller.get_battery()
print("Battery level:", levels)    
   
# Each motor can be configured to operate at a specific speed. To retrieve the configured speed you use the get_speed function. 
speed=faller.get_speed(faller.MotorCrab)
print(speed)

# Each motor can be configured to operate at a specific speed. To retrieve the configured speed you use the get_speed function. 
newspeed=faller.set_speed(faller.MotorCrab, speed=50)
print(newspeed)

# To change the configured speed for a motor you can also provide a speed difference to the change_speed function.
# the value returned is the new speed. 
newspeed = faller.change_speed(faller.MotorChassis, diff=5)
print(newspeed)
