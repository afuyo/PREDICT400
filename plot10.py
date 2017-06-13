# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from math import *


x = np.linspace(-15, 15, 100)
y=-5.0*x-(15.0/x)
plt.figure()
plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()