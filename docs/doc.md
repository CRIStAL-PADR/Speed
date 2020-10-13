	 This document is written as part of the Speed project in order to understand how the requests are sent to the microcontroller aisp 12F by pc and the corresponding action to this request. In this contest  we will proceed to a reverse engineering
	Here is a list of command generated after a test

 => The engine 1 is for horizontal move (for the Chassis and the Crab)
 => The engine 2 is for the vertical move (for the spreader)

 => The spreader is connected to the address 172.17.217.61
 => The crab is connected to the address 172.17.217.61
 => The Chassis is connected to address  172.17.217.217 
1- stopM: This command allow us to stop  moteur. We can thus select the engine we want to stop (for example engine 1 : StopM?sNr=1) 


2- startM : This command allow us to select the engine we want to run and also his direction (for example engine 2 : startM?sNr=1&turn=1)

3- changePWMTV: this command allow us to change the ryclic ratio (for example engine 1 : changePWMTV?sNr=1&diff=5) in order to modify the speed

	=> The line 2 and 3 are necesseraie to run the engine

4- getBat : This command allow us to see the state of the batteries after an action(for example getBat?n=2)

5- getConf 

6- fswitchConf

7- getOtherEsp : This allow us to connect to the microcontroller



