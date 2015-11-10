Getting Started
========================================

Dependencies
----------------------------------------
You will need to install (at least) the following Python modules:

* PySerial_ - For serial (RS232) communication.

* Matplotlib_ - For 2D visualization.

Each of these Python projects has directions on how to download and install.  For Ubuntu there are packages that you can install with a package manager like Synaptic.

.. _PySerial: http://pyserial.sourceforge.net/
.. _Matplotlib: http://matplotlib.org/

Installation
----------------------------------------
There really is no installation.  You should just check-out the latest revision from the SVN repository at https://bbingham.svn.cloudforge.com/pici

Overview and Theory of Operation
----------------------------------------
TBD

First Steps
----------------------------------------
There are two examples of very simple controllers:

1. ''control_wallavoid.py'' is an example for interacting with the Create via serial. You will need to connect the compter to the Create via serial for this to work.  You should be able to run this program from the command line::

 $ python control_wallavoid.py

2. ''sim_test.py'' is an example of a simple controller interacting with the simulation environment. Note that you'll need to close the figure window and do a CNTRL+C to kill the program if you don't want to wait for it to expire.  Again, you can run this directly from the command line::

 $ python sim_test.py









