from drawer import *
def f(x):
    return x*x*0.1
x_start = -50
x_finish = 50


axes()
to_point(x_start,f(x_start))
pen_down()

for x in range(x_start,x_finish+1):
    to_point(x, f(x))



