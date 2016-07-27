import tkinter as t


def fu(event):
    me = event.widget
    if me == button1:
        print('b1')

def fur():
    print('ololo')


def init_main_window():
    global root, button1, button2, label, text, ruler
    root = t.Tk()

    #способ 1 - не биндим, используем command. Кнопка срабатывает как кнопка, с пробела, и по отпусканию кнопки мыши
    button1 = t.Button(root, text = "Йя кнопко", command=fur)
    #button1.bind("<Button>", fu)  #<Button-1> левая кнопка мыши, 3-правая


    #Способ 2 - забиндить кнопку. Срабатывает на нажатие (а не на отпускание) кнопки мыши
    #и не нажимается пробелом
    button2 = t.Button(root, text = "Йя попко")
    button2.bind("<Button>", fu)  #<Button> любой кнопкой мыши
    variable = t.IntVar()
    label = t.Label(root, text = 'Тут лейбл')
    ruler = t.Scale(root)
    text = t.Entry(root)
    for obj in button1, button2, label, text, ruler:
        obj.pack()


if __name__ == "__main__":
    global root

    init_main_window()
    root.mainloop()
