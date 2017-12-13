from numpy import *
a = array([1,2,3,4])
print a
print a.dtype
print type(a)
b = array([1,32,4,5], dtype=float)
print b
print b.dtype

c = zeros((3,4))
print c.dtype

print arange(10,30,4)
print linspace(1,0,5)
print float(54)
print int8(43.7)
set_printoptions(threshold='nan')  
print arange(10000).reshape(100,100)
print dtype(bool).itemsize
print a.ndim
print a.size
print a.dtype.name

aa = [12,4,3,4,5]
print aa
bb = aa
bb[0] = 0
print aa
print bb
import copy
cc = copy.copy(aa)
cc[0]=100
print aa
print cc
dd = type(cc)(cc)
print dd
dd[0] =101
print dd
print cc
print list(cc)
