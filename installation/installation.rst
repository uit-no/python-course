

============
Installation
============

You need a recent version of Python 3 installed. At the very least, version 3.3.
Version 3.5 is recommended. You can check the version you have installed
with::

  $ python3 --version


Option 1: Anaconda (good for beginners)
=======================================

Go to https://www.continuum.io/downloads and download the Python 3.5 version
for your system.


Windows
-------

Install Python 3 using all of the defaults for installation but make sure to
check "Make Anaconda the default Python".


Mac OS X
--------

Install Python 3 using the defaults for installation.


Linux
-----

In your terminal run the installer that
you just downloaded, e.g.::

  $ bash Anaconda3-4.0.0-Linux-x86_64.sh

If you answer "yes" to the question
"Do you wish the installer to prepend the Anaconda3 install location
to PATH in your /home/user/.bashrc ?"
then this will make the Anaconda distribution the default Python.
You can always undo this by editing your .bashrc.
Otherwise you go with the defaults.


Option 2: Virtual Environments (Linux or Mac OS X)
==================================================

For this make sure that you have virtualenv installed.
This also assumes that Python is installed on the system.
See also http://docs.python-guide.org/en/latest/dev/virtualenvs/.

Go to https://github.com/uit-no/python-course
and download the repository as zip file (click
on "Download ZIP" on the right).

Then extract the zip file and inside python-course-master
you can install all requirements using::

  $ python3 -m venv venv
  $ source venv/bin/activate
  $ pip install -r installation/requirements.txt

We recommend this approach to seasoned users. This because a possible pitfall
with this approach is that some of the pip packages need C compilation, which
depends on a number of system packages that pip can't install. If the "pip
install" step fails with compilation errors, then you likely don't have some
required C libraries installed on your system.


Option 3: Vagrant
=================

If you are familiar with `Vagrant <https://www.vagrantup.com>`_, then a Linux
virtual machine with everything you need is just a "git clone" and a "vagrant
up" away.

First, download and unpack or clone the `course repository
<https://github.com/uit-no/python-course>`_ from github. Then, open a terminal,
cd to the directory in which you have unpacked or cloned the repository, and
run::

    vagrant up

In a couple of minutes, you'll have a VM that has everything installed. Log in
to the machine and look around like so::

    vagrant ssh

Then, once you are logged in::

    cd /vagrant
    ls

One thing you will for sure like to do is to start `jupyter
<http://jupyter.org/>`_, which we use in the course for some presentations and
exercises::

    cd /vagrant
    ./run_jupyter.sh

Now just point your browser to http://localhost:8888
