from drawer import *
from math import sin
from time import sleep

def f(x):
    return 90*sin(x*0.09)
x_start = -150
x_finish = 150


axes()
to_point(x_start,f(x_start))
pen_down()

for x in range(x_start,x_finish+1):
    to_point(x, f(x))

sleep(10)



