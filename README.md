# Fallerlib
A python library to control Faller (c) 180290 models. 

Example
-------
```python
from speedlib import fallerlib as cranelib
cranelib.init("172.17.217.217")
cranelib.set_speed(fallerlib.MotorChassis, 50)
cranelib.step(fallerlib.MotorChassis, fallerlib.MotorDirectionBackward)
```
You can find more examples in the *examples* directory.

Install
-------
git clone https://github.com/CRIStAL-PADR/Speed.git

The library is in fallerlib/fallerlib.py

Tests
-----
To starts the unit tests you can do:
```console
cd tests/
PYTHONPATH=../fallerlib python3 -m unittest
```

