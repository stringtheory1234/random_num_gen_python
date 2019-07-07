import random
from tkinter import *
window = Tk()
window.title("Random number generator")
window.configure(background="black")

labelText = StringVar()
labelText.set("")
label = Label(window, textvariable=labelText, bg="black", fg="white", font="none 16 bold")
label.grid(row=3, columnspan=6, pady=10)

def RandGen():
    a = number1.get()
    b = number2.get()
    if a=='' or b=='' :
        labelText.set("Can't Leave a or b empty")
    elif int(a)>int(b) :
        labelText.set("b should be >= a")
    else :
        x = random.randint(int(a), int(b))
        labelText.set("")
        labelText.set("Random number generated is: "+str(x))
labela = Label(window, text="a: ", bg="black", fg="white", font="none 20 bold")
labela.grid(row=0)
number1 = Entry(window, width=10)
number1.grid(row=0, column=1)


labelb = Label(window, text="b: ", bg="black", fg="white", font="none 20 bold")
labelb.grid(row=0, column=2)
number2 = Entry(window, width=10)
number2.grid(row=0, column=3)


label = Label(window, text="click the button to generate a random number: ", bg="black", fg="white", font="none 20 bold")
label.grid(row=1, padx=10, pady=10, columnspan=6)

b1 = Button(window, text="Generate It!", width=10, command=RandGen)
b1.grid(row=2, columnspan=6, pady=10)

window.mainloop()