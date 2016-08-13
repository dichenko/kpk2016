import tkinter

def paint(event):
    """ Обработчик событий для холста
    :param event: событие
    :return: ничего
    """
    print(event.x, event.y)
    canvas.coords(line, 0,0,event.x, event.y)

root = tkinter.Tk()
canvas = tkinter.Canvas(root, background='yellow', width=400, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

for i in range(10):
    canvas.create_oval(i*40, i*40, i*40+30, i*40+30, fill='green', width='0')

line = canvas.create_line(0,0,10,100)

















root.mainloop()