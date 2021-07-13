from speedlib.dcc import dcc_object, dcc_switches
from speedlib.dcc.dcc_object import DCCObject
from speedlib.dcc .dcc_switches import Switch


# Create the DCC controller with the RPi encoder, Create a switch (args: Name, DCC Address, biais_id)
#  and Register locos on the controller
S = Switch("DCC",3, 1)
dcc_object.start() #Start the controller. Removes brake signal

print(S.biais)

S.biais = True #change the state of the biais

S.set_biais_id(2) #choose the biais 2
S.biais = True
S.biais = False
dcc_object.stop()

