infinite
========

*itertools operations on infinite generators*

Description
-----------

Some of the ``itertools`` operations do not work on infinite generators,
this package is the beginning of the work to port some of the iterator
concepts to the infinity.

``infinite`` is compatible with both python2 and python3.

Installation
------------

The package has been uploaded to `PyPI`_, so you can
install the package using pip:

    pip install infinite

Usage
-----

For example if we want to iterate all the pairs of natural numbers:

.. code:: python

    from itertools import count
    from infinite import product

    for x, y in product(count(0), count(0)):
        print(x, y)
        if (x, y) == (3, 3):
            break

.. _PyPI: https://pypi.python.org
