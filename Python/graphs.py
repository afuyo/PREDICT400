import matplotlib.pyplot
from matplotlib.pyplot import *
import numpy 
from numpy import linspace

# The example shows how to plot a system of consistent equations.
# This is Example 1 Section 2.1 of Lial.  The function linspace divides the
# interval [-1,15] into 100 points. For each value in x, y1 and y2 will have
# a corresponding value based on the calculations shown below.

#x= linspace(0,200,100)
#y1= 0.25*x +30
#y2= 0.3*x +25

# Plots can be built up in layers.  What follows shows how to plot individual
# colored lines.  plt.legend will associate the indicated equations to the 
# preceding plt.plot statements.  The order of appearance must be the same. 
# loc=3 places the legend in the lower left corner.
#figure()
#xlabel('x-axis')
#ylabel('y-axis')
#plot (x, y1, 'r')
#plot (x, y2, 'b')
#legend (('Plan A y=0.25x +30','Plan B y=0.3x +25'),loc=4)
#title ('Comparing Cell Phone Companies')
#show()

x=linspace(0,100,20)
y1=30.0- 0.66*x
y2=60.0- 1.5*x
figure()
xlabel('x-axis')
ylabel('y-axis')
plot (x,y1,'r')
plot (x,y2,'b')
legend(('2x+3y=90','3x+2y=120'),loc='best')
show()
x=linspace(0,100,20)
y1=21-1.5*x
y2=12-0.4*x
y3=8
figure()
xlabel('x-axis')
ylabel('y-axis')
plot (x,y1,'r')
plot (x,y2,'b')
plot(x,y3,'g')
legend(('30x+20y=420','10x+25y=300','0x+1y=8'),loc='best')
show()