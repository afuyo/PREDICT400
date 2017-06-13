# -*- coding: utf-8 -*-
import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import arange
figure()
#ax = add_subplot(111)
x= arange(-1,10,1)
y= arange(-1,10,1)
y1= 27.0 - 3.0*x
y2= 12.0-1.0*x
y3=15.0 - 1.5*x
#y1= 12.0 - 2.0*x
#y2= 6.0 - 0.5*x
xlabel('x1-axis')
ylabel('x2-axis')
title (' Feasible Region')

plot(x,y1,color='b')
plot(x,y2,color='r')
plot(x,y3,color='g')
legend(['0.3x1 + 0.1x2=2.7','0.5x1 + 0.5x2=6', '0.6x1+0.4x2=6'])

xlim(-1,10)
ylim(-1,10)
grid(True)
x= [6.0,7.5,8.0]
y= [6.0,4.5, 3.0]
fill(x,y)
show()