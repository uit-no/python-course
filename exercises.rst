

Exercises
=========

Below you find the source code for the exercises.
Copy and paste them into a file called e.g. ``basics.py``.
It is OK to copy all or just one or two exercises
to start with. We give you the tests and you need
to code the functions to make the tests pass.
It is OK to work in pairs and it is OK to use
Google and Stack Overflow.

You can run the tests like this::

  $ py.test -vv basics.py

You can also run a single test, e.g.::

  $ py.test -vv -k test_reverse_list basics.py


Basics
------

Make the following tests green:

.. literalinclude:: exercises/basics.py
   :language: python
   :linenos:


List comprehensions
-------------------

Imagine you need a list of all Pythagorean triples up to n = 20 which happens
to be (you remember the triangles from school)::

  [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20)]

Try to implement the list of all such triples
using a list comprehension in one single line of Python code.
Use a variable for the upper bound such that if you one day
need all Pythagorean triples up to n = 2000 you only need to change
one line of code.


Higher-order functions
----------------------

Make the following tests green:

.. literalinclude:: exercises/higher-order.py
   :language: python
   :linenos:

Using the ``upper()`` method you can uppercase text:

.. code-block:: python

  assert 'zZzZzzZzzZzZ'.upper() == 'ZZZZZZZZZZZZ'

Now try to uppercase a string using your ``simple_map()`` (replace the "?"
with some meaningful code):

.. code-block:: python

  assert ''.join(simple_map(?, 'zZzZzzZzzZzZ')) == 'ZZZZZZZZZZZZ'


Generators
----------

Implement a function ``simple_range(n)`` which returns a list ``[0, 1, 2, ..., n-1]`` such that
(do not use the built-in ``range`` function):

.. code-block:: python

  assert simple_range(5) == [0, 1, 2, 3, 4]
  assert simple_range(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Now what do you think will happen when you call ``simple_range(100000000)``?

Rewrite your function using the generator pattern and discuss
the advantages.


Decorators
----------

Consider the following code:

.. code-block:: python
  :linenos:

  def add(a, b):
      return a + b

  def subtract(a, b):
      return a - b

  i = add(2, 3)
  j = subtract(2, 3)

Now implement a decorator "debug" such that when you decorate
the ``subtract`` function and execute this script:

.. code-block:: python
  :linenos:
  :emphasize-lines: 4

  def add(a, b):
      return a + b

  @debug
  def subtract(a, b):
      return a - b

  i = add(2, 3)
  j = subtract(2, 3)

You obtain::

  $ python example.py

  function "subtract" called with arguments: 2 3
