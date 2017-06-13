# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from math import *


x = np.linspace(-15, 15, 100)
#y= 12000.0/(1.0+19.0*np.exp(-1.2*x))
y=-5*x-(15/x)
plt.figure()
plt.plot(x, y)
plt.xlabel('$x$')
plt.ylabel('$\exp(x)$')


plt.show()