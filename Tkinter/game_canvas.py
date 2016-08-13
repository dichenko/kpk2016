import tkinter

def click_ball(event):
    """ Обработчик событий для игрового холста
    :param event: событие с координатами клика
    :return: ничего
    """

    canvas.coords(line, 0,0,event.x, event.y)

def create_random_ball():
    """

    :return:
    """
    pass
    canvas.create_oval(x, y, x+2*r, y+2*r, fill=random_color, width='0')


root = tkinter.Tk()
canvas = tkinter.Canvas(root, background='yellow', width=400, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

for i in range(10):
    canvas.create_oval(i*40, i*40, i*40+30, i*40+30, fill='green', width='0')



















root.mainloop()