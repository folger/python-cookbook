xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
from itertools import zip_longest
for i in zip_longest(a, b):
    print(i)
for i in zip_longest(a, b, fillvalue=0):
    print(i)
