from math import *
# -*- coding: utf-8 -*-
#The population of students at Northwestern is given by the formula
#𝑝�p(t)=(𝑡t^2+100)∗ln (t𝑡+2) , where t represents the time in years since 2000. 
#Using Python, find the rate of change of the student population in both 2006 and 2016.

#p´(t)=2tln(t+2)+(t^2+100/x+2)
#number of years from 2000

def p(t):
    return 2.0*t*log(t+2.0)+((t**2+100)/t+2)
print p(6)
print p(16)
