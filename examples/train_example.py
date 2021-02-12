from speedlib.trains import dcc
from speedlib.trains.dcc import Train



train1 = Train("DCC3",3) # Create the DCC controller with the RPi encoder, Create locos (args: Name, DCC Address) and Register locos on the controller
train2 = Train("DCC1",1)

dcc.start() #Start the controller. Removes brake signal

train1.l.speed = 14 # set de speed to 14
train1.slower() # Reduce speed by one step
train1.reverse() #
train1.l.fl = True # Change fl function bit and allows to light it
train1.l.f2 = False
dcc.stop() # Stop the controller

