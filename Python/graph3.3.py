import matplotlib.pyplot
from matplotlib.pyplot import *
import numpy 
from numpy import linspace


x=linspace(0,60,20)
y1=21-1.5*x
y2=12-0.4*x
y3=8 +0*x
figure()
xlabel('x-axis')
ylabel('y-axis')
plot (x,y1,'r')
plot (x,y2,'b')
plot(x,y3,'g')
legend(('30x+20y=420','10x+25y=300','0x+1y=8'),loc='best')
show()