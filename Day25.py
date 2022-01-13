from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry('620x620')
root.title("TicTacToe")

x=ImageTk.PhotoImage(Image.open('images/x.png').resize((200, 200)))
o=ImageTk.PhotoImage(Image.open('images/o.png').resize((200, 200)))

def X(button):
	button.config(image=x)

padx,pady=95,95
cerocero = Button(root, padx=padx, pady=pady,command=lambda: X(cerocero))
cerocero.grid(row=0, column=0)
onecero = Button(root, padx=padx, pady=pady,command=lambda: X(onecero))
onecero.grid(row=1, column=0)
twocero = Button(root, padx=padx, pady=pady,command=lambda: X(twocero))
twocero.grid(row=2, column=0)
ceroone = Button(root, padx=padx, pady=pady,command=lambda: X(ceroone))
ceroone.grid(row=0, column=1)
oneone = Button(root, padx=padx, pady=pady,command=lambda: X(oneone))
oneone.grid(row=1, column=1)
twoone = Button(root, padx=padx, pady=pady,command=lambda: X(twoone))
twoone.grid(row=2, column=1)
cerotwo = Button(root, padx=padx, pady=pady,command=lambda: X(cerotwo))
cerotwo.grid(row=0, column=2)
oneTwo = Button(root, padx=padx, pady=pady,command=lambda: X(oneTwo))
oneTwo.grid(row=1, column=2)
twoTwo = Button(root, padx=padx, pady=pady,command=lambda: X(twoTwo))
twoTwo.grid(row=2, column=2)

root.mainloop()