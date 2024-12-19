from tkinter import *
from random import randint
BLUE = "#0000ff"
GREEN = "#9bdeac"
RANGE = 4
num_1 = None
num_2 = None

def randoms():
    global num_1
    global num_2
    num_1 = randint(1,RANGE)
    num_2 = randint(1, RANGE)
    canvas.itemconfig(operation_display, text=f"{num_1} * {num_2}")


window = Tk()
window.minsize(width=350,height=280)
window.configure()
window.grid()

image = PhotoImage(file="beach.png")
canvas = Canvas()
canvas.create_image(200,200,image=image)
operation_display = canvas.create_text(200,30,text="",font=("Courier",30,"normal" ),fill=GREEN)
canvas.grid(column=0,row=1)

check = Button()
check.configure(text="Sprawdz",command=randoms,background=BLUE,fg=GREEN)
check.grid(column=0,row=5,sticky=[E,W])

entry = Entry()
entry.focus()
entry.configure(width=10)
entry.place(x=160,y=245)








window.mainloop()