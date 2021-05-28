from tkinter import *

def addCat(event):
    global pets
    pets['cats'] = pets['cats'] + 1
    updateDisplay()

def addDog(event):
    global pets
    pets['dogs'] = pets['dogs'] + 1
    updateDisplay()

def addHamster(event):
    global pets
    pets['hamsters'] = pets['hamsters'] + 1
    updateDisplay()

def addOther(event):
    global pets
    content = txtBox.get()
    txtBox.delete(0, 'end')

    if content.lower() not in pets:
        pets[content.lower()] = 1
    else:
        pets[content.lower()] = pets[content.lower()] + 1
    updateDisplay()

def reset(event):
    global pets

    for i in pets:
        pets[i] = 0

    updateDisplay()

def updateDisplay():
    global pets

    outputStr = 'There are '

    for i in pets:
        outputStr += '{0} {1}, '.format(pets[i], i)

    ##Function to display results##
    outputLbl.configure(text = outputStr)

pets = { 'cats': 0, 'dogs': 0, 'hamsters': 0 }

window = Tk()#create the window#
window.title("Jacob's")
# Code to add widgets will go here...
##Setup frames##
topframe = Frame(window)
topframe.pack()

bottomframe = Frame(window)
bottomframe.pack(side = BOTTOM)
##setup label to display output in top frame##
welcome = Label(topframe, fg="red", font=("Helvetica", 16), text = "Welcome to Cat or Dog Selector")
welcome.pack()

outputLbl = Label(topframe, text = "0")
outputLbl.pack()
#setup  buttons in grid layout within bottom frame##
catBtn = Button(bottomframe, text='Cat')
catBtn.bind("<1>", addCat)
catBtn.grid(row=0, column=1)

dogBtn = Button(bottomframe, text='Dog')
dogBtn.bind("<1>", addDog)
dogBtn.grid(row=0, column=2)

hamBtn = Button(bottomframe, text='Hamster')
hamBtn.bind('<1>', addHamster)
hamBtn.grid(row=0, column=3)

txtBox = Entry(bottomframe)
txtBox.grid(row=2, column=2)
submit = Button(bottomframe, text='Submit')
submit.bind('<1>', addOther)
submit.grid(row=2, column=3)

r = Button(bottomframe, text='Reset')
r.bind('<1>', reset)
r.grid(row=1, column=2)

# Code to add widgets ends. Mainloop keeps program running whilst waiting for user input##
window.mainloop()
