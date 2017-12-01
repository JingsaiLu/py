import copy

a = [1,2,3,[4,5]]
print a
b = a
b[0] = 10
print a
print b
c = copy.copy(a)
print c
c[1] = 20
print 'a=', a
print 'b=', b
print 'c=', c
c[3][0] = 20
print 'a=', a
print 'b=', b
print 'c=', c
