import tkinter



def paint(event):
    """ Обработчик событий для холста
    :param event: событие
    :return: ничего
    """
    print(event.x, event.y)
    canvas.coords(line, 0,0,event.x, event.y)

root = tkinter.Tk()
canvas = tkinter.Canvas(root)
canvas.bind("<Motion>", paint)
canvas.pack()


line = canvas.create_line(0,0,10,100)















root.mainloop()