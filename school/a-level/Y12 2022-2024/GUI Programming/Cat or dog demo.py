from tkinter import *

def addCat(event):
    global cat
    cat = cat + 1
    updateDisplay()

def addDog(event):
    global dog
    dog += 1
    updateDisplay()

def resetCat(event, update = True):
    global cat
    cat = 0

    if update: updateDisplay()

def resetDog(event, update = True):
    global dog
    dog = 0

    if update: updateDisplay()

def reset(event):
    resetCat(False)
    resetDog(False)

    updateDisplay()

def updateDisplay():
    global cat, dog

    cats = f'{cat} ' + ('cat' if cat == 1 else 'cats')
    dogs = f'{dog} ' + ('dog' if dog == 1 else 'dogs')
    isAre = 'is' if cat == 1 else 'are'

    outputLabel.configure(text = f'There {isAre} {cats}, and {dogs}.')

cat = 0
dog = 0

window = Tk("Cat or Dog")

topFrame = Frame(window)
topFrame.pack()

bottomFrame = Frame(window)
bottomFrame.pack(side = BOTTOM, pady = 10)

welcome = Label(topFrame, fg="red", font=("Helvetica", 16), text = "Welcome to Cat or Dog Selector")
welcome.pack()

outputLabel = Label(topFrame, text = "0")
outputLabel.pack()

catButton = Button(bottomFrame, text='Cat')
catButton.bind("<1>", addCat)
catButton.bind("<3>", resetCat)
catButton.grid(row = 0, column = 0, padx = 10)

dogButton = Button(bottomFrame, text='Dog')
dogButton.bind("<1>", addDog)
dogButton.bind("<3>", resetDog)
dogButton.grid(row = 0, column = 2, padx = 20)

resetButton = Button(bottomFrame, text='Reset', bg='#000000', fg='#ffffff')
resetButton.bind("<1>", reset)
resetButton.grid(row = 0, column = 3)

updateDisplay()

window.mainloop()
