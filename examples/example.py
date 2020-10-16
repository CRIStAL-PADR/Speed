# -*-coding: <Utf-8> -*-

"""
 Here is an example of how to use the fallerlib library and the functions that we can perform with it 
 
"""

import fallerlib
import time

 
#This line allows the initialization of the master's IP address and launches a second request to obtain the slave's IP address.

IP = "172.17.217.217"
fallerlib.init(IP)

#We can possibly check that we have the IP address of the slave we expected with the fallerlib.get_other_esp (IP) function
t = fallerlib.get_other_esp(IP)
print(t)
#This test returns the IP address of the slave to us => the initialization was successfull"""



#Suppose we want to move the crab, frame and spread simultaneously.
#See help (fallerlib.start) for more information on the parameters that this function takes
# The code to do this is as follows

fallerlib.start(fallerlib.MotorSpreader, fallerlib.MotorDirectionForward)
fallerlib.start(fallerlib.MotorCrab, fallerlib.MotorDirectionBackward)
fallerlib.start(fallerlib.MotorChassis, fallerlib.MotorDirectionForward)


#Suppose we want to move the MotorCrab or one of the motor for 5 seconds. The code to do it is as follows
# But before writing the code First we have to import time librairy (see line 9)
init_time = time.time()

while (time.time() -init_time )< 5:
    x = fallerlib.start(fallerlib.MotorCrab, fallerlib.MotorDirectionBackward)
    print(time.time() -init_time )
   
    

# After executing a function like moving the motorCrab for 5 seconds, if we want for example to know the state of the battery here is the code

for i in fallerlib.get_battery():
    print("....",i)
    
    
#Suppose we want to move the MotorChassis forward in a given direction and we want to know its current speed to change it or not. 
#To to that we'll use the get_speed function. here is a code to do that 

t = fallerlib.get_speed(fallerlib.MotorCrab)
print(t)

#Once we know the current speed we can decide to modify it
#For this we will use the change_speed function as shown in the following example
#It can also be displayed on the screen using the print function

t= fallerlib.change_speed(fallerlib.MotorChassis, 30)
print(t)



