from speedlib.dcc import dcc_object, dcc_switches
from speedlib.dcc.dcc_object import DCCObject
from speedlib.dcc .dcc_switches import Switch


# Create the DCC controller with the RPi encoder, Create a switch (args: Name, DCC Address, biais_id)
#  and Register locos on the controller
S = Switch("DCC",3)
dcc_object.start() #Start the controller. Removes brake signal

print(S.biais)

S.biais = [dcc_switches.biais1, True] #change the state of the biais

S.biais = [dcc_switches.biais2, True] 
S.biais = [dcc_switches.biais1, True] 
dcc_object.stop()

