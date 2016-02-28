#!/usr/bin/python
"""
File: Lagrange_poly2b.py

Copyright (c) 2016 Michael Seaman

License: MIT

Implements the past Lagrange poly modules and tests them out with
f(x) = abs(x)
"""

import Lagrange_poly2 as poly2
import math

poly2.graph(math.fabs, 2, -2, 2)
poly2.graph(math.fabs, 4, -2, 2)
poly2.graph(math.fabs, 6, -2, 2)
poly2.graph(math.fabs, 10, -2, 2)

poly2.graph(math.fabs, 13, -2, 2)
poly2.graph(math.fabs, 20, -2, 2)

