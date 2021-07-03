a=5
b=0

try:
    print(a/b)
except ZeroDivisionError:
    print("the divisor can't be 0")

m=3
n="1"

try:
    print(m+n)
except TypeError:
    print("numbers can't calculated with strings")