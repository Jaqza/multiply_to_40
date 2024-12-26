from tkinter import *
from random import randint
BLUE = "#0000ff"
GREEN = "#9bdeac"
LOWER_RANGE = 4
UPPER_RANGE = 10
num_1 = None
num_2 = None

def label_clear():
    entry.delete(0, END)
    entry.focus()

def canvas_clear():
    canvas.itemconfig(congratulation_display, text="")
    canvas.itemconfig(feedback, text=f"")

def randoms():
    global num_1
    global num_2
    num_1 = randint(2,LOWER_RANGE)
    num_2 = randint(2, UPPER_RANGE)
    canvas.itemconfig(operation_display, text=f"{num_1} * {num_2}")

def result_check():
    result = int(num_1) * int(num_2)
    if entry.get() == str(result):
        canvas.itemconfig(congratulation_display, text="Brawo", fill= GREEN)
        canvas.itemconfig(feedback, text=f"{num_1} * {num_2} = {result}" ,fill = GREEN)
        label_clear()
        window.after(3000, canvas_clear)
    else:
        canvas.itemconfig(congratulation_display, text="Cwicz dalej" , fill= "red")
        canvas.itemconfig(feedback, text=f"{num_1} * {num_2} = {result}", fill= "red")
        label_clear()
        window.after(3000, canvas_clear)
    window.after(3000, randoms)

window = Tk()
window.minsize(width=350,height=280)
window.configure()
window.grid()

image = PhotoImage(file="beach.png")
canvas = Canvas()
canvas.create_image(200,200,image=image)
operation_display = canvas.create_text(200,30,text="",font=("Courier",30,"normal" ),fill=GREEN)
congratulation_display = canvas.create_text(200,205,text="",font=("Courier",30,"normal" ),fill=GREEN)
feedback = canvas.create_text(200, 240, text="",font=("Courier",30,"normal" ))
canvas.grid(column=0,row=1)
window.after(2500, randoms)

entry = Entry()
entry.focus()
entry.configure(width=10)
entry.place(x=160,y=105)

check = Button()
check.configure(text="Sprawdz",command=result_check,background=BLUE,fg=GREEN)
check.grid(column=0,row=5,sticky=[E,W])

# window.bind("<Return>", result_check) this needs to wait

window.mainloop()