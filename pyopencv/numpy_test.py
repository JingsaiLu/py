import numpy as np

# print np.version.version
# print np.array([1,2,3,4])
# print np.array([[1,2,3],[1,2,3]])
# print np.array((1,2,3,4,5,6))
# print np.array((1.2,2,3,4))
# print np.array((1.2,2,3,4), dtype=np.int32)
# print np.arange(15)
# print np.arange(15).reshape(3,5)
# print np.linspace(1,3,9)
# print np.zeros((3,4))
# print np.ones((3,4))
# print np.eye(3)
a = np.ones((100,100,3))
print a.size
b = a[0:30,0:30]
print b.size