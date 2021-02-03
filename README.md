# SpeedLib
A python library to operate Speed devices.

Currently only the Faller (c) 180290 models is supported. 

Example
-------
```python
from speedlib.cranes import faller
from speedlib.cranes.faller import Crane
ip_1 = "172.17.217.217"
ip_2 = "172.17.217.217"
crane_1 = Crane()
crane_2 = Crane()
crane_1.init(ip_1)
crane_2.init(ip_2)
crane_2.start_for(20*faller.ureg.millisecond,faller.MotorChassis,faller.MotorDirectionForward)
crane_1.change_speed(faller.MotorCrab, -40)
```
You can find more examples in the *examples* directory.

Install
-------
git clone https://github.com/CRIStAL-PADR/Speed.git

The library is in speedlib/__init__.py

Tests
-----
To starts the unit tests you can do:
```console
cd tests/
PYTHONPATH=../ python3 -m unittest
```

