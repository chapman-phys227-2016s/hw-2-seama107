#!/usr/bin/python
"""
File: Lagrange_poly1

Copyright (c) 2016 Michael Seaman

License: MIT

Lagrange's interpolation model, modeling a continuous function
with a polynomial model
"""

import numpy as np
import math


def p_L(x, xp, yp):
    L_outputs = np.array([L_k(x, k, xp) for k in np.arange(len(xp))])
    return np.sum(yp * L_outputs)
    

def L_k(x, k, xp):
    k_index_removed = np.append(xp[:k],xp[k+1:])
    elements = (x - k_index_removed)/( float(xp[k]) - k_index_removed)
    return np.prod(elements)


def test_p_l(xp = np.linspace(0,math.pi, 5), yp = np.array([math.sin(y) for y in np.linspace(0,math.pi, 5)]) ):
    teststatus = True
    for x in np.nditer(xp):
        x = p_L(x, xp, yp)
    for i in xrange(len(xp)):
        print xp[i], yp[i]
        if ( not (xp[i] < yp[i] + .005 and xp[i] > yp[i] - .0000005)):
            teststatus = False
    assert(teststatus)

