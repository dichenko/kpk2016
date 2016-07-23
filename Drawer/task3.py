from drawer import *

for y1 in range(5):
    for y2 in range(5):
        pen_up()
        to_point(0,y1*50)
        pen_down()
        to_point(100,y2*50)



