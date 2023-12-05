from tkinter import *


class UserInterface(Tk):
    def __init__(self):
        super().__init__()
        self.title = "Tic Tac Toe"

        self.buttons = []
        self.create_grid()
        self.label = Label(text="deneme")
        self.label.grid(row=0, column=1)

        self.mainloop()

    def create_grid(self):
        for i in range(1, 4):
            for j in range(3):
                new_button = Button(width=15, height=10)
                new_button.grid(row=i, column=j)
                self.buttons.append(new_button)

