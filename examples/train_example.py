
from speedlib.dcc import dcc_object, dcc_trains
from speedlib.dcc.dcc_object import DCCObject
from speedlib.dcc .dcc_trains import Train



train1 = Train("DCC3",3) # Create the DCC controller with the RPi encoder, Create locos (args: Name, DCC Address) and Register locos on the controller

dcc_object.start() #Start the controller. Removes brake signal

train1.speed = 5 # set the speed to 14
train1.slower() # Reduce speed by one step
train1.faster() # Increase speed by one step
train1.f_light = True # Change fl function bit and allows to light it
train1.f2 = True
print(train1) # Print train1 information
dcc_object.stop() # Stop the controller
