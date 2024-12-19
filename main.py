from tkinter import *#
from random import randint
BLUE = "#0000ff"
GREEN = "#9bdeac"
RANGE = 4
num_1 = None
num_2 = None
def operation_display_delay():
    canvas.itemconfig(operation_display, text=f"{num_1} * {num_2} = ??")
    canvas.itemconfig(congratulation_display, text="")
    canvas.itemconfig(result_display, text="")

def randoms():
    global num_1
    global num_2
    num_1 = randint(1,RANGE)
    num_2 = randint(1, RANGE)
    window.after(3000,operation_display_delay)


def check():
    global num_1
    global num_2
    multiply = int(num_1) * int(num_2)
    comparator = int(data.get())
    if multiply == comparator:
        canvas.itemconfig(congratulation_display, text="Bravo" , fill= "white")
        canvas.itemconfig(result_display, text=f"{num_1} * {num_2} = {multiply}", fill="white")

    else:
        canvas.itemconfig(congratulation_display, text="niestety :/", fill="red")
        canvas.itemconfig(result_display, text=f"{num_1} * {num_2} = {multiply}", fill="red")

    clear_text()
    entry.focus()
    randoms()
def clear_text():
    entry.delete(0, 'end')

def it_has_been_written(*args):
    data.trace_add("write", it_has_been_written)

window = Tk()
window.minsize(width=350,height=280)
window.configure()
window.grid()

image = PhotoImage(file="beach.png")
canvas = Canvas()
canvas.create_image(200,200,image=image)
operation_display = canvas.create_text(200,30,text="",font=("Courier",30,"normal" ),fill=GREEN)
congratulation_display = canvas.create_text(200,100,text="",font=("Courier",30,"normal" ),fill="red")
result_display = canvas.create_text(200,210,text="",font=("Courier",30,"normal" ),fill=GREEN)
canvas.grid(column=0,row=1)

randoms()

check_button = Button()
check_button.configure(text="Sprawdz",background=BLUE,fg=GREEN,command=check)
check_button.grid(column=0,row=5,sticky=[E,W,N])

data = StringVar()
entry = Entry(textvariable=data)
entry.focus()
entry.configure(width=10,validatecommand=it_has_been_written)
entry.place(x=160,y=245)


window.mainloop()