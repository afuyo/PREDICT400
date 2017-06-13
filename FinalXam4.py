from math import *
# -*- coding: utf-8 -*-
#The population of students at Northwestern is given by the formula
#ğ‘í±¡p(t)=(ğ‘¡t^2+100)âˆ—ln (tğ‘¡+2) , where t represents the time in years since 2000. 
#Using Python, find the rate of change of the student population in both 2006 and 2016.

#pÂ´(t)=2tln(t+2)+(t^2+100/x+2)
#number of years from 2000

def p(t):
    return 2.0*t*log(t+2.0)+((t**2+100)/t+2)
print p(6)
print p(16)
