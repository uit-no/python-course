

Exercises
=========

Below you find the source code for the exercises.
Copy and paste them into a file called e.g. ``basics.py``.
It is OK to copy all or just one or two exercises
to start with. We give you the tests and you need
to code the functions to make the tests pass.

You can run the tests like this::

  $ py.test -vv basics.py

You can also run a single test, e.g.::

  $ py.test -vv -k test_reverse_list basics.py


Basics
------

.. literalinclude:: exercises/basics.py
   :language: python
   :linenos:


Higher-order functions
----------------------

.. literalinclude:: exercises/higher-order.py
   :language: python
   :linenos:


Generators
----------

Implement a function ``simple_range(n)`` which returns a list ``[0, 1, 2, ..., n-1]`` such that
(do not use the built-in ``range`` function):

.. code-block:: python

  assert simple_range(5) == [0, 1, 2, 3, 4]
  assert simple_range(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

Now what do you think will happen when you call ``simple_range(100000000)``?

Rewrite your function using the generator pattern and discuss
the advantages.
