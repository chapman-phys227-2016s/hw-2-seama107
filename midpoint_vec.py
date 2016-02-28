#!/usr/bin/python
"""
File: midpoint_vec.py

Copyright (c) 2016 Michael Seaman

License: MIT

Compares the runtimes of python sum, python for loop summation
and numpy vectorized sum on the midpoint integral formula.
"""

import numpy as np

def midpointint(f, a, b, n):
    """
    Computes the Midpoint integration rule of f from a to b using a python for loop. 
    """
    running_sum = 0
    for i in range(n):
        running_sum += f(a + ((b-a)/float(n))*(i + .5) )
    return running_sum * (b-a)/float(n)

def return_midpoint_values(f, a, b, n):
    """
    Helper function for python and numpy sum
    """
    output = []
    for i in range(n):
        output.append(f(a + ((b-a)/float(n))*(i + .5) ))
    return output

def midpointint_python_sum(f, a, b, n):
    """
    Computes the Midpoint integration rule of f from a to b using the python sum function
    """
    midpoint_values = return_midpoint_values(f, a, b, n)
    output_sum = sum(midpoint_values)
    return output_sum * (b-a)/float(n)

def midpointint_numpy_sum(f, a, b, n):
    """
    Computes the Midpoint integration rule of f from a to b using the numpy sum function
    """
    midpoint_values = return_midpoint_values(f, a, b, n)
    output_sum = np.sum(midpoint_values)
    return output_sum * (b-a)/float(n)

def test_int_accuracy():
    assert int(midpointint(function, 0, 3, 10)+.5) == 9

def test_intpython_accuracy():
    assert int(midpointint_python_sum(function, 0, 3, 10)+.5) == 9

def test_intnumpy_accuracy():
    assert int(midpointint_numpy_sum(function, 0, 3, 10)+.5) == 9

def function(x):
    return x*2
