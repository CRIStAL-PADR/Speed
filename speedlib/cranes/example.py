from dccpi import *
import dcc
from dcc import Train

train1 = Train("DCC4",4)
train2 = Train("DCC1",1)
dcc.start()
train1.speed(10)
train1.stop()


