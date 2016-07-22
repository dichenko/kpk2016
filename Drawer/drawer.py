from turtle import Turtle

def init_drawman():
    global t, x_current, y_current
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)

def test_drawman():
    """Тестирование работы Чертежника"""
    pen_down()
    on_vector(100,0)
    on_vector(0,-100)
    on_vector(-100,0)
    on_vector(0,100)
    pen_up()



def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(dx, dy):
    global x_current
    x_current += dx
    global y_current
    y_current += dy
    t.goto(x_current,y_current)

def to_point(x,y):
    global x_current
    x_current = x
    global y_current
    y_current= y
    t.goto(x,y)

if __name__ == '__main__':
    init_drawman()
    test_drawman()