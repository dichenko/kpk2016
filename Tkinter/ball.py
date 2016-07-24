import tkinter as t
root = t.Tk()

def fu(event):

    me = event.widget
    if me == button1:
        print('b1')


button1 = t.Button(root, text = "Йя кнопко")
button1.bind("<Button>", fu)  #<Button-1> левая кнопка мыши, 3-правая
button1.pack()

button2 = t.Button(root, text = "Йя попко")
button2.bind("<Button>", fu)  #<Button> любой кнопкой мыши
button2.pack()



root.mainloop()
