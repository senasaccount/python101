import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])

a, b, c = np.split(x, (3,6))

print("a = ",a)
print("b = ",b)
print("c = ",c)

##

k = np.arange(16).reshape(4,4)

print("k = ",k)

upperar, lowerar = np.vsplit(k, [2]) #vsplit stands for vertical split

print("upperar = ",upperar)
print("lowerar = ",lowerar)

upperar2, lowerar2 = np.hsplit(k, [2]) #hsplit stands for horizontal split

print("upperar2 = ",upperar2)
print("lowerar2 = ",lowerar2)

##

l = np.random.normal(10, 2, (3,3))

print("l = ",l)

print(np.sort(l, axis=0)) #sorted column-wise
print(np.sort(l, axis=1)) #sorted row-wise

##

t = np.arange(10, 20)

print("t = ",t)
print("t[0::2] = ",t[0::2])
print("t[1::3] = ",t[1::3])

##

d = np.random.randint(-1, 10, (5,5))

print("d = ", d)

print(d[:, 0]) #all row are selected, whereas only the first column is selected
print(d[:, 3]) #same here, just another column is selected
print(d[2, :])
print(d[0:3, 0:2])

##

f = np.random.randint(0, 10, size= (5, 5))

print("f = ",f)

copy = f[0:1, 0:3].copy()
#copy function provides to not changing the original values of the main array (which is f here) 
print("copy = ",copy)
print("f = ",f)

##

#fancy index

g = np.arange(15, 0, -2)
print("g = ", g)

bring = [2, 5, 3]
print("g[bring] = ",g[bring])

##

h = np.arange(16).reshape(4,4)
print("h = ", h)

row = np.array([2, 1])
column = np.array([2, 2])

print("h[row, column] =", h[row, column])
print("h[2, [1, 2]] =", h[2, [1, 2]])
print("h[0:, h[1, 2]] =" , h[0:, [1, 2]])

##

j = np.arange(10)
print(j)

print(j<6)
print(j[j!=4])

##

# 4*x1 + x2 = 15
# 6*x1 + 2*x2 = 8   solve the two equations

q = np.array([[4, 1], [6, 2]])
w = np.array([15, 8])

print(np.linalg.solve(q, w))