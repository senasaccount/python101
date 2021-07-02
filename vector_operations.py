a=[1,2,3,4]
b=[3,4,5,6]

ab=[]

for i in range(0, len(a)):
    ab.append(a[i]*b[i])

print(ab)

#or it could be interpreted also in numpy, like:

import numpy as np

a=np.array([1,2,3,4])
b=np.array([3,4,5,6])

print(a*b)