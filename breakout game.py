from tkinter import *

import time, random


tk = Tk()
tk.title("Swag")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

tk.mainloop()
