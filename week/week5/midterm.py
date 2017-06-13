import numpy 
from numpy import *
from numpy.linalg import *


#
A =[[1, 0, 1], [4, 1, -2], [3, 1, -1]]
A= matrix(A)
print ('\nMatrix A')
print A

# Numpy has various functions to perform matrix calculations.  The inverse
# function inv() is one of those.

# Find inverse of A.
print ('\nInverse of A')
IA= inv(A)
print IA
##########################

##1b1b1b

A =[[1, 2, 3], [3, 1, 2], [2, 0, 1]]
A= matrix(A)
xyz=[18,23,13]
xyz=matrix(xyz)
xyz=transpose(xyz)
IA=inv(A)
result=dot(IA,xyz)
print result

################33
A =[[2, 4, 2], [2, 1, 2], [2, 1, 3]]
A= matrix(A)
xyz=[72,48,60]
xyz=matrix(xyz)
xyz=transpose(xyz)
IA=inv(A)
#result=dot(IA,xyz)
result=dot(IA,A)
print result

A=[[1,2,3],[-3,-2,-1],[-1,0,1]]

A=matrix(A)


IA=inv(A)
print IA
result=dot(IA,A)
print result
##############################

#2
B=[[3,1,2],[3,2,1],[2,1,2]]
B=matrix(B)
IB=inv(B)
result =dot(B,IB)
print result

#result = dot(IB,xyz)
xyz=[90000,50000,61000]
xyz=matrix(xyz)
xyz=transpose(xyz)
#########

B=[[3,3,2],[1,2,1],[2,1,2]]
B=matrix(B)
IB=inv(B)
result =dot(IB,B)
print result

result = dot(IB,xyz)
xyz=[810,410,490]
xyz=matrix(xyz)
xyz=transpose(xyz)
print result