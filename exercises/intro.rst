

======
Basics
======

Link to the exercises: https://github.com/uit-no/python-course/blob/master/exercises/intro.py

You can fetch them to your computer with::

  $ wget https://raw.githubusercontent.com/uit-no/python-course/master/exercises/intro.py

To run the test suite you need to install pytest::

  $ virtualenv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt

You can run the tests like this::

  $ py.test -vv intro.py

You can also run a single test, e.g.::

  $ py.test -vv -k test_reverse_list intro.py
