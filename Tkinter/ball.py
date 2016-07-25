import tkinter as t
root = t.Tk()

def fu(event):
    me = event.widget
    if me == button1:
        print('b1')

def fur():
    print('ololo')

#способ 1 - не биндим, используем command. Кнопка срабатывает как кнопка, с пробела, и по отпусканию кнопки мыши
button1 = t.Button(root, text = "Йя кнопко", command=fur)
#button1.bind("<Button>", fu)  #<Button-1> левая кнопка мыши, 3-правая
button1.pack()


#Способ 2 - забиндить кнопку. Срабатывает на нажатие (а не на отпускание) кнопки мыши
#и не нажимается пробелом
button2 = t.Button(root, text = "Йя попко")
button2.bind("<Button>", fu)  #<Button> любой кнопкой мыши
button2.pack()



button1['text'] = 'Я текст'

root.mainloop()
