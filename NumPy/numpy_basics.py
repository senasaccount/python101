import numpy as np
from numpy.core.fromnumeric import ndim, size

print(np.zeros(5, dtype=int))

print(np.ones((4,7), dtype=float))

print(np.full((6,8), 9))

print(np.arange(4,65, 7))

print(np.linspace(1.2, 3, 8))

print(np.random.normal(3, 2, (4,4))) #3 is the mean, where 2 is the standart deviation

print(np.random.randint(0, 15, (6,7)))

a=np.random.randint(10, size=10)

print("a = ",a)

print(a.ndim)
#ndim is for indicate the dimension

print(a.shape)
#in the output 10 stands for the number of numbers

print(a.size)

print(a.dtype)

b=np.random.randint(10, size=(4,3))

print("b = ",b)

print(b.ndim)

print(b.shape)

print(b.size)

print(b.dtype)

m=np.arange(1,10)
print(m)

n=np.reshape(m,(3,3))
print(n.ndim)

x=np.array([1,2,3])
y=np.array([4,5,6])

print(np.concatenate([x,y]))

z=np.array([[1,2,3],
            [4,5,6]])

print(np.concatenate([z,z]))
print(np.concatenate([z,z], axis=0))
print(np.concatenate([z,z], axis=1))