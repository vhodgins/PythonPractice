from tkinter import *
import time




tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)


def movetrigangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(1, -5, 0)
    elif event.keysym == 'Right':
        canvas.move(1, 5, 0)



canvas.bind_all('<KeyPress-Up>', movetrigangle)
canvas.bind_all('<KeyPress-Down>', movetrigangle)
canvas.bind_all('<KeyPress-Right>', movetrigangle)
canvas.bind_all('<KeyPress-Left>', movetrigangle)



tk.mainloop()
