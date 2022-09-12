#lambda that returns products of elements of a list
from functools import *
a = [1, 2, 3, 4, 5,8,7]
w = reduce(lambda x, y:x+y, a)
c = reduce(lambda x, y:x-y, a)
print(w)