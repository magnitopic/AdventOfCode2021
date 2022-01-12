from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('900x900')
root.title("TicTacToe")

x=PhotoImage(file='images/x.png')
o=PhotoImage(file='images/o.png')

def X(button):
	button.config(image=x)


cerocero = Button(root, padx="120", pady="150",command=lambda: X(cerocero))
cerocero.grid(row=0, column=0)
onecero = Button(root, padx="120", pady="150",command=lambda: X(onecero))
onecero.grid(row=1, column=0)
twocero = Button(root, padx="120", pady="150",command=lambda: X(twocero))
twocero.grid(row=2, column=0)
ceroone = Button(root, padx="120", pady="150",command=lambda: X(ceroone))
ceroone.grid(row=0, column=1)
oneone = Button(root, padx="120", pady="150",command=lambda: X(oneone))
oneone.grid(row=1, column=1)
twoone = Button(root, padx="120", pady="150",command=lambda: X(twoone))
twoone.grid(row=2, column=1)
cerotwo = Button(root, padx="120", pady="150",command=lambda: X(cerotwo))
cerotwo.grid(row=0, column=2)
oneTwo = Button(root, padx="120", pady="150",command=lambda: X(oneTwo))
oneTwo.grid(row=1, column=2)
twoTwo = Button(root, padx="120", pady="150",command=lambda: X(twoTwo))
twoTwo.grid(row=2, column=2)

root.mainloop()