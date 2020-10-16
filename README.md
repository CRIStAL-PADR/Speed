# fallerlib
A library to control Faller (c) models. 

The library is in fallerlib/fallerlib.py

Tests
-----
To starts the tests you can do:

```console
cd tests/
PYTHONPATH=../fallerlib python3 -m unittest
```

#Suppose we want to move the MotorCrab or one of the motor for 5 seconds. The code to do it is as follows
# But before writing the code First we have to import time librairy
init_time = time.time()

while (time.time() -init_time )< 5:
    x = fallerlib.start(fallerlib.MotorCrab, fallerlib.MotorDirectionBackward)
    print(time.time() -init_time )
   
