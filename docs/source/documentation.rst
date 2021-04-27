Speedlib documentation
======================

**SPEEDLIB** is a python library developped as a part of the SPEED project which allows us to control trains with the DCC protocol 
as well as the portic of the faller brand. It is made up of 2 librairies:
* The trains librairies which controls the trains
* The cranes library which controls the cranes

Trains library
--------------

The principle of this library is based on the ** DCC ** protocol.

DCC
---

**DCC** ( *digital control system* ) is a standard used in model railroading to control individual locomotives or track accessories by modulating 
the supply voltage of the track.

The locomotives and their accessories (lights, effects) as well as the network accessories each have a unique address. 
The coded signal sent on the track gives commands to the equipment while providing power.

Principle
---------

The role of the **DCC** standard is to generate an electrical signal in binary to send information to locomotives or accessories. 
A sequence of 0 and 1 which are electrically translated by long positive and negative alternations (100us) for the 0 and short (58us) for the 1. 
The terminals on the circuit (locomotives and accessories) are equipped with decoders that translate these binary messages into commands.
A zero bit is also made up of two consecutive halfwaves the duration of which is defined as
more complex way. The nominal duration of an alternation is between 100µs and 9900µs and the sum of
two vibrations must not exceed 12000µs (12ms).