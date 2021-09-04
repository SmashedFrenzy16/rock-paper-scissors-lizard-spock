from tkinter import *
import random

root = Tk()

listofoutcomes = ["Computer: Rock", "Computer: Paper", "Computer: Scissors", "Computer: Lizard", "Computer: Spock"]

choice = random.choice(listofoutcomes)


def execute1():
    label = Label(root, text="You: Rock |")
    label.grid(row=0, column=1)
    label1 = Label(root, text=choice)
    label1.grid(row=0, column=2)


def execute2():
    label = Label(root, text="You: Paper |")
    label.grid(row=0, column=1)
    label1 = Label(root, text=choice)
    label1.grid(row=0, column=2)


def execute3():
    label = Label(root, text="You: Scissors |")
    label.grid(row=0, column=1)
    label1 = Label(root, text=choice)
    label1.grid(row=0, column=2)

def execute4():
    label = Label(root, text="You: Lizard |")
    label.grid(row=0, column=1)
    label1 = Label(root, text=choice)
    label1.grid(row=0, column=2)

def execute5():
    label = Label(root, text="You: Spock |")
    label.grid(row=0, column=1)
    label1 = Label(root, text=choice)
    label1.grid(row=0, column=2)

button1 = Button(root, text="Rock", command=execute1)
button2 = Button(root, text="Paper", command=execute2)
button3 = Button(root, text="Scissors", command=execute3)
button4 = Button(root, text="Lizard", command=execute4)
button5 = Button(root, text="Spock", command=execute5)

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
button4.grid(row=3, column=0)
button5.grid(row=4, column=0)


root.mainloop()
