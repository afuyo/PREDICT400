# -*- coding: utf-8 -*-
import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import arange
figure()
#ax = add_subplot(111)
x= arange(-10,50,10)
y= arange(-10,50,10)
y1= 10.0 + 0.0*x
y2= 50.0-2.0*x
x1=40.0+0.0*y
#y1= 12.0 - 2.0*x
#y2= 6.0 - 0.5*x
xlabel('x-axis')
ylabel('y-axis')
title (' Feasible Region')

plot(x,y1,color='b')
plot(x,y2,color='r')
plot(x1,y,color='g')
xlim(-10,50)
ylim(-10,50)
hlines(0,-10,50,color='k')
vlines(0,-10,50,color='k')
grid(True)
x= [0.0,0.0, 20.0, 25.0]
y= [0.0,10.0, 10.0, 0.0]
fill(x,y)
show()