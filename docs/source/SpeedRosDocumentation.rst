
======================
SpeedRos documentation
======================

SpeedRos is a version of Speedlib which offers us the possibility to control miniature devices like Faller (c) Crane, DCC trains or Switches using ROS.

Software requirements 
=====================
In addition to the speedlib software requirements, SpeedRos to work requires:

* Ubuntu mate
* `speedlib`: Install and download  `speedlib <https://cristal-padrspeed.readthedocs.io/en/latest/documentation.html#installation>`_

* `ROS` : Install `ROS <http://wiki.ros.org/ROS/Installation>`_


Hardware requirements
=====================
Same for speedlib see : speedlib Hardware requirements

Building a SpeedRos workspace and sourcing the setup file
=========================================================
* Knowing how to use ROS

.. note::
    Before starting, it is imperative to create a local working directory in which to clone the remote repository of SpeedROS . Once it's done, you have to build 
    the packages in the SpeedRos workspace 

.. code-block:: console

    $ cd ~/.../SpeedRos
    $ catkin_make

Once the workspace was built, it created a similar structure in the devel subfolder which you usually find under / opt / ros / $ ROSDISTRO_NAME

To add the workspace to your ROS environment you need to source the generated setup file:

.. code-block:: console
    
    $ source ~/.../SpeedRos/devel/setup.bash

It should be noted that this will only work for cranes. In order to correctly source the generated setup file,
because of the wiringPi used to control the trains and the switches, you must be in sudo :

.. code-block:: console

    $ sudo su

Once it's done we can now control our devices

Controlling a Faller (c) crane model using ROS
==============================================

You must first check that you are connected to the faller's wifi.

Open a terminal and run the following command:

.. code-block:: console

    $ roscore

Open a second terminal and run the following command:

.. code-block:: console
    
    $ rosrun crane crane_pilotpy "172.17.217.217"

Open a third terminal and run the following command:

.. code-block:: console
    
    $ rostopic pub /crane/command std_msgs/String " data : '' "

.. note::

    "172.17.217.217" is the ip address of the crane faller card I used.
    It is required to connect to the crane.
    If yours is different, please put the one corresponding to your crane. (See faller datasheet)

Example
-------
For the start_for method here is the command:

.. code-block:: console

    $ rostopic pub /crane/command std_msgs/String " data : ' crane_command : start_for; value : 5; motors_name : MotorChassis; motors_direction : MotorDirectionForward' "

For the set_speed method here is the command: 

.. code-block:: console

    $ rostopic pub /crane/command std_msgs/String " data : ' crane_command : set_speed; speed_value : 5; motors_name : MotorChassis' "


Controlling a DCC train and switch model
========================================

..note ::
    You must first be an administrator to be able to control the train or the switch because of the wiringPiSetup
    It is also essential to source the setup file (see Building a SpeedRos workspace and sourcing the setup file)

Train
-----
Open a terminal and run the following command:

.. code-block:: console

    $ roscore

Open a second terminal and run the following command:

.. code-block:: console
    
    $ rosrun train train_pilotpy 8 3

.. note::
    The first parameter is the number of train that we want to initialize. The second parameter designates the address 
    or number of the first train to be initialized

Open a third terminal and run the following command:

.. code-block:: console
    
    $ rostopic pub /train/command std_msgs/String " data : '' "

Example
~~~~~~~

For the faster method here is the command:

.. code-block:: console
    
    $ rostopic pub /train/command std_msgs/String " data : 'train_command : faster; train_number : 3' "

For the speed method here is the command :

.. code-block:: console
    
    $ rostopic pub /train/command std_msgs/String " data : 'train_command : speed; train_number : 5; speed_value : 15' "

For the fl method here is the command:

.. code-block:: console
    
    $ rostopic pub /train/command std_msgs/String " data : 'train_command : fl; train_number : 5; accessories_value : True' "

Switch
------

Open a terminal and run the following command:

.. code-block:: console

    $ roscore

Open a second terminal and run the following command:

.. code-block:: console

    $ rosrun switch switch_pilot.py 8 3

.. note::
    Like the train, the first parameter is the number of switch that we want to initialize. The second parameter designates the address or number of the first switch to be initialized

Open a third terminal and run the following command:

.. code-block:: console
    
    $ rostopic pub /switch/command std_msgs/String " data : '' "

Example
~~~~~~~

For the biais method here is the command:

.. code-block:: console
    
    $ rostopic pub /switch/command std_msgs/String " data : 'switch_command : biais; switch_number : 6; biais_id : 1; biais_state : True' "

To print information about the switch her is the command :

.. code-block:: console
    
    $ rostopic pub /switch/command std_msgs/String " data : 'switch_command : biais_info; switch_number : 6' "

For the debugging
=================

Usually we can use the tab to help us enter the ros command lines. However, sometimes the tab does not work. This can be due to 2 potential errors:

* the node file is not an executable. To correct this, just write in the terminal: 
    .. code-block:: console
        
        $ chmod + x file.py

* the Setup file is not well sourced.

.. note::
    We can also use a debugging command to find out if the ros node that we have launched has been properly initialized

    .. code-block:: console
        
        $ roswtf

This command allows you to know which ros nodes are running on the machine.