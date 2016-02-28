#!/usr/bin/python
"""
File: fit_pendulum_data

Copyright (c) 2016 Michael Seaman

License: MIT

Gets data about a pendulum and fits it using the numpy
polynomial approximator
"""
import numpy as np
import matplotlib.pyplot as plt

def retrieve_pendulum_data(filename = "pendulum.dat"):
    """
    Gets pendulum data from filename and outputs a 2d list of
    output[0] = L and output[1] = T
    """
    L_list = []
    T_list = []
    with open(filename, 'r') as infile:
        for line in infile:
            data = line.split()
            try:
                L_list.append(float(data[0]))
                T_list.append(float(data[1]))
            except ValueError:
                pass
            
    infile.close()
    return [L_list, T_list]

def pendulum_fit(L, T, degree):
    """
    Outputs the original list of lengths and a list of period variables as given by the fitted function T(L)
    """
    coeff = np.polyfit(L, T, degree)
    p = np.poly1d(coeff)
    print "Fitted Curve of degree {0}: ".format(degree)
    print p
    return [L,p(L)]


