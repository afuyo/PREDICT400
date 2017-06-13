import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import *



x= arange(0,20.1,0.1)
y0= arange(0,20.1,0.1)
y1= 20.0-2.0*x
y2= 15.0-x
# The definition of y3 will allow filling the unbounded region in the plot.
y3= 20+0.0*x
# The filling will be between y3 and the maximum of y1 and y2.  Need to define 
# a new array y4 which will be that maximum.

y4=[0]*len(x)
for k in range(0,len(x)):
    if y1[k] >= y2[k]:
        y4[k]=y1[k]
    if y2[k] > y1[k]:
        y4[k]=y2[k]

# Plot limits must be set for the graph.
xlim(0,20)
ylim(0,20)

# Plot axes need to be labled,title specified and legend shown.
xlabel('x-axis')
ylabel('y-axis')
title('Shaded Area Shows the Feasible Region')

plot(x,y2,color='b')
plot(x,y1,color='r')
legend(['y=15-x','y=20-2x'])


fill_between(x,y3,y4, color='grey',alpha=0.2)
show()