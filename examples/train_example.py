from speedlib.trains import dcc
from speedlib.trains.dcc import Train



train1 = Train("DCC3",3) # Create the DCC controller with the RPi encoder, Create locos (args: Name, DCC Address) and Register locos on the controller
train2 = Train("DCC1",1)

dcc.start() #Start the controller. Removes brake signal

train1.speed = 5 # set the speed to 14
train1.slower() # Reduce speed by one step
train1.faster() # Increase speed by one step
train1.fl = True # Change fl function bit and allows to light it
train1.f2 = True
print(train1) # Print train1 information
print(train2)  # Print train2 information
dcc.stop() # Stop the controller

