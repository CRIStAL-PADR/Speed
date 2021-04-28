Speedlib documentation
======================

**SPEEDLIB** is a python library developped as a part of the SPEED project which allows us to control trains with the DCC protocol 
as well as the portic of the faller brand. It is made up of 2 librairies:
* The trains librairies which controls the trains
* The cranes library which controls the cranes

Trains library
==============

The principle of this library is based on the **DCC** protocol.

DCC
---

**DCC** (*digital control system*) is a standard used in model railroading to control individual locomotives or track accessories by modulating 
the supply voltage of the track.

The locomotives and their accessories (lights, effects) as well as the network accessories each have a unique address. 
The coded signal sent on the track gives commands to the equipment while providing power.

Principle
^^^^^^^^^

The role of the **DCC** standard is to generate an electrical signal in binary to send information to locomotives or accessories. 
A sequence of 0 and 1 which are electrically translated by long positive and negative alternations (100us) for the 0 and short (58us) for the 1. 
The terminals on the circuit (locomotives and accessories) are equipped with decoders that translate these binary messages into commands.
To send an order to a decoder bits (0 or 1) are put together to form packets.

Structure of a package
^^^^^^^^^^^^^^^^^^^^^^

In order for the decoder to find its way around, it is necessary to respect a message format that it will be able to interpret and
perform if intended. This format comes in the form of a packet.
Each packet begins with a header or preamble, a kind of start of packet announcement, is followed by one or two bytes  of address, 
then comes the instruction and finally the validity check or checksum.

The preamble is made up of at least 10 consecutive bits at 1. It is used by decoders to synchronize themselves.
on the beginning of a message. Then come a separator bit at 0 to announce the message itself, and
the byte containing the address of the decoder for which this command is intended. We will return
later on this addressing system. A 0 separator bit precedes the instruction byte. In
some cases there may be several bytes always separated by a bit at 0.

To end the packet we find the control byte calculated by the command station. She performs the bit by bit sum, 
that is to say without holding, of each of the bytes of the message and places the result at the end of the message.
The decoder will perform the same operation to check the validity of the message received before interpreting it. The end of
packet is indicated by a terminator bit which happens to always be 1. The next packet will start with a
preamble and so on… The packets are transmitted by the command station and follow one another without stopping. He
There are several types of packages: packages for locos, reset, filling.

Équipments 
----------
* A control unit consisting of an electronic board and a motor board whose purpose is to modulate the track voltage.
* Mobile (locomotives ) or fixed equipment (lights) that are equipped with decoders to interpret control signals.

The control center
^^^^^^^^^^^^^^^^^^       
It can be either manual or automated.
For automation there are control software available under linux.
As control software we can use:

* an Atmega 328 /2560 microcontroller.
* an Arduino Uno / Mega
* RaspberryPI 

The motor board (the booster)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The choice to use an engine card is motivated by the fact that Arduino or RaspberryPi cards are not able to provide enough power.
However, the principle of the DCC standard is to circulate "control" information in the power circuit (the rails), hence the importance of having a engine board.
As a choice of motor board we will use LMD18200. This board keeps the shape of the voltage of the signal present at their input (so the information) 
and amplifies the output signal. The shape of the impulses is kept in order to keep the transmitted codes.

In the case of the speedlib project, we will use the RaspberryPI.

Hardware requirements 
---------------------

La RaspberryPI utilise une librairie `dccpi <https://pypi.org/project/dccpi/>`_ développé par  `Hector Sanjuan <https://github.com/hsanjuan?tab=overview&from=2017-12-01&to=2017-12-31>`_
This module implements the DCC protocol for controlling model trains using a Raspberry Pi.It is able to output direction and speed DCC-encoded packets on one 
of the RPi GPIO pins. It needs WiringPi libraries to work.

