import tkinter
import random


ball_initial_number = 10
ball_minimum_radius = 15
ball_maximum_radius = 40
ball_available_colors = ["green","blue","red"]


def click_ball():
    """ Обработчик событий для игрового холста
    :param event: событие с координатами клика
    :return: по клику нужно удалять тот объект на который мышка показывает
    А также засчитывать его в очки
    """
    pass
    #FIXME

def create_random_ball():
    """
    Создает шарик в случайном месте игрового холста Canvas
    при этом шарик не выходит за границы холста
    :return:
    """
    r = random.randint(ball_minimum_radius,ball_maximum_radius)
    x = random.randint(0+r, int(canvas['width'])-1-r)
    y = random.randint(0+r, int(canvas['height'])-1-r)
    canvas.create_oval(x, y, x+2*r, y+2*r, fill=random_color(), width='0')

def random_color():
    """
    Возвращает случайный цвет из набора цветов
    :return:
    """
    return random.choice(ball_available_colors)

def init_main_window():
    global root, canvas
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, background='yellow', width=400, height=400)
    canvas.bind("<Motion>", click_ball())
    canvas.pack()

def init_ball_catch_game():
    """
    Создает мячики
    :return:
    """
    for i in range(ball_initial_number):
        create_random_ball()

if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()