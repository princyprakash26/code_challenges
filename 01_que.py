

#convert radians into degrees

import math

def func(n):
    radian = n
    radian_degree = radian * (180/math.pi)
    return radian_degree
x = func(1)
print(x)
