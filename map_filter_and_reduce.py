list1=[1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda x: x+5, list1)))

print(list(filter(lambda x: x%5==0, list1)))

from functools import reduce

print(reduce(lambda a,b: a+b, list1))