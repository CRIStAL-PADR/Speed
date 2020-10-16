# Fallerlib
A python library to control Faller (c) 180290 models. 

Example: 
--------
Suppose we want to move the MotorCrab or one of the motor for 5 seconds. The code to do it is as follows
But before writing the code First we have to import time librairy

```python
import fallerlib
fallerlib.init("172.17.217.217")
fallerlib.set_speed(fallerlib.MotorChassis, 50)
fallerlib.step(fallerlib.MotorChassis, fallerlib.MotorDirectionBackward)
```

Install:
--------
git clone https://github.com/CRIStAL-PADR/Speed.git
The library is in fallerlib/fallerlib.py

Tests
-----
To starts the unit tests you can do:
```console
cd tests/
PYTHONPATH=../fallerlib python3 -m unittest
```

