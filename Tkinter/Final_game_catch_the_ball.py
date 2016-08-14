from tkinter import *
from random import *

root = Tk()
canvas = Canvas(root)
canvas.pack()


def create_scores_text():
    global scores_text
    scores_text = canvas.create_text(60, 12,
                                     text="Scores: " + str(scores),
                                     font="Sans 18")


def change_scores_text():
    canvas.itemconfigure(scores_text, text="Scores: " + str(scores))


def generate_random_ball_coord():
    x = randint(r, screen_width-r)
    y = randint(r, screen_height-r)
    return x, y


def generate_random_ball_velocity():
    vx = randint(-10, +10)
    vy = randint(-10, +10)
    return vx, vy


def create_ball():
    global x, y, vx, vy, ball
    x, y = generate_random_ball_coord()
    vx, vy = generate_random_ball_velocity()
    ball = canvas.create_oval(x - r, y - r, x + r, y + r, fill="green")


def move_ball():
    global x, y, vx, vy
    new_x, new_y = x - vx, y - vy
    if new_x < r or new_x > screen_width - r:
        new_x = x  # rolling back coordinate!
        vx = -vx
    if new_y < r or new_y > screen_height - r:
        new_y = y  # rolling back coordinate!
        vy = -vy
    canvas.move(ball, new_x - x, new_y - y)
    x, y = new_x, new_y


def flick_ball():
    global x, y, vx, vy
    new_x, new_y = generate_random_ball_coord()
    vx, vy = generate_random_ball_velocity()
    canvas.move(ball, new_x - x, new_y - y)
    x, y = new_x, new_y


def time_event():
    move_ball()
    canvas.after(100, time_event)


def mouse_click(event):
    global scores
    if (event.x - x)**2 + (event.y - y)**2 <= r**2:
        scores += 1
        change_scores_text()
        flick_ball()


scores = 0
x = y = 0  # not needed
r = 50
screen_width = int(canvas["width"])
screen_height = int(canvas["height"])

create_ball()
create_scores_text()
canvas.bind('<Button-1>', mouse_click)
time_event()  # начинаю циклически запускать таймер
root.mainloop()