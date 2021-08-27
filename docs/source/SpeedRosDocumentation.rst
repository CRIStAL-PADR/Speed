
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
