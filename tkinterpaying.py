from tkinter import *
import random


def random_rect(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2)


'''def hello():
    random_rect(400, 400)

    tk2 = Tk()
    btn = Button(tk2, text="Fuck my ass!", command=hello)
    btn.pack()
    '''


tk = Tk()
canvas = Canvas(tk, width=1000, height=1000)
canvas.pack()
canvas.create_text(900, 100, text='swag... epic epic swag', fill='red', font=('', 15))
my_image = PhotoImage(file='c:\\Users\\v3hod\\Desktop\\smiley.png')
canvas.create_image(0, 0, anchor=NW, image=my_image)
tk.mainloop()

