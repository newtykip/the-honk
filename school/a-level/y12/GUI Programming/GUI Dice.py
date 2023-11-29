import tkinter as tk
from tkinter.font import Font, BOLD
from random import randint

class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.sides = 6
        self.sum = 0
        self.geometry('500x500')
        self.updateTitle()

        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.option_add('*font', Font(self, size = 12))
        self.tk_setPalette(background = 'white')

        container = tk.Frame()
        container.grid(row = 0, column = 0, sticky = '')

        sideController = tk.Frame(master=container)
        sideController.grid(row = 3, column = 0)

        self.outputLabel = tk.Label(container, font=Font(self, size = 25, weight = BOLD))
        self.sumLabel = tk.Label(container, font=Font(self, size = 20))
        self.sidesLabel = tk.Label(sideController)

        rollButton = tk.Button(container, text='Roll!')
        decrementSides = tk.Button(sideController, text = '←', borderwidth = 0)
        incrementSides = tk.Button(sideController, text = '→', borderwidth = 0)

        self.outputLabel.grid(row = 0, column = 0, pady=(0, 20))
        self.updateOutput()

        self.sumLabel.grid(row = 1, column = 0, pady=(0, 50))
        self.updateSum()

        rollButton.bind("<1>", self.roll)
        rollButton.grid(row = 2, column = 0, pady=(0, 30))

        decrementSides.bind("<1>", self.decrementSides)
        decrementSides.grid(row = 0, column = 0)

        self.sidesLabel.grid(row = 0, column = 1)
        self.updateSides()

        incrementSides.bind("<1>", self.incrementSides)
        incrementSides.grid(row = 0, column = 2)

    def updateOutput(self, roll = 'N/A'):
        self.outputLabel.configure(text = roll)

    def updateSum(self):
        self.sumLabel.configure(text = f'Sum: {self.sum}')

    def roll(self, _):
        number = randint(1, self.sides)
        self.updateOutput(number)

    def updateTitle(self):
        self.wm_title(f'{self.sides}-sided Dice')

    def updateSides(self):
        self.sidesLabel.configure(text = self.sides)
        self.updateTitle()

    def decrementSides(self, _):
        self.sides -= 1

        if self.sides < 2:
            self.sides = 2

        self.updateSides()

    def incrementSides(self, _):
        self.sides += 1

        self.updateSides()

Window().mainloop()