Speedlib documentation
======================

**SPEEDLIB** is a python library developped as a part of the SPEED project which allows us to control trains with the DCC protocol 
as well as the portic of the faller brand. It is made up of 2 librairies:
* The trains librairies which controls the trains
* The cranes library which controls the cranes

Warning
^^^^^^^
Since Speedlib is made up of two libraries, one for trains and the other for cranes, the library using trains
only works on a RaspberryPI. It would be preferable to install Speedlib directly on a RaspberryPI in order to be able
to use the train and crane API.

Installation
-------------
To install Speedlib, open a new Terminal window and type the following command

>>> pip install speedlib

Software requirements
---------------------
* python_requires= '>=3.6'
* bitstring module details. Should be auto-fetched when installing with pip.
* wiringPi: download and install `wiringPi <http://wiringpi.com/download-and-install/>`_
* Since wiringPi uses low-level mechanisms to access pins, dccpi programs must be run as root


Trains library
==============





Cranes library
=============