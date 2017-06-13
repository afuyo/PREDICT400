import math 
# calculate sum x
n= 10 #number of elements
x=[20,30,40,50,60,70,80,90,100,110]
sum_x=sum(x)
#calculate sum y
y=[71.2,80.5,73.4,60.3,52.1,56.2,46.5,36.9,34.0,39.1]
sum_y=sum(y)
#calculate sum xy
xy=[]
for a,b in map(None,x,y):
    xy.append(int(a*b))
   

sum_xy=sum(xy)
#calculate sum x square
x_sq=map(lambda s: s**2,x)
sum_x_sq=sum(x_sq)

#calculate sum y square
y_sq = map(lambda s: s**2,y)
sum_y_sq=sum(y_sq)





#formula for calculating r

#values to be used in denominator

a=n*sum_x_sq-sum_x**2
b=n*sum_y_sq-sum_y**2

r= ((n*sum_xy) - (sum_x*sum_y))/(math.sqrt(a)*math.sqrt(b))
r=round(r,3)

print "Correlation coefficient r on accidental death rates is r = %s"%r

