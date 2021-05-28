#-------------------------------------------------------------------------------
# Name:        calculator v1.2 - decimal point added
# Purpose:      calculator using TKinter
#
# Author:      L Jacob
#
# Created:     23/07/2015
# Copyright:   (c) L Jacob 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from decimal import Decimal

##Functions for mathematic operations##
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a,b):
    return a * b

def updateDisplay(update):
    ##Function to display results##
    outputLbl.configure(text = str(update))

def handlerEquals(event):
    ##Event handler for equals button##
    ##Function requires operand to be specified so that correct operation is performed##
    global first_num ## use the variable of this name that has been created outside of this function, i.e. our 'global' variable
    global second_num
    global operand

    ##convert user inputs to numbers ready to do the maths##
    first_num = Decimal(first_num)
    second_num = Decimal(second_num)

    if operand != None:
        if operand == '+':
            result = add(first_num,second_num)
        elif operand == '-':
            result = subtract(first_num,second_num)
        elif operand == '/':
            if second_num == 0:
                result = 'You can not divide by zero!'
                first_num = None
                second_num = None
                operand = None
            else:
                result = divide(first_num,second_num)
        elif operand == '*':
            result = multiply(first_num,second_num)
        updateDisplay(result)

def handlerOperand(event):
    ##Event Handler for operation buttons##
    ##Function to store users choice of add, subtract, divide, multiply##
    global operand
    caller = event.widget['text'] #get the text value of the button that is passed in to the handler
    if operand == None:
        operand = caller
        updateDisplay(0)
    else:
        pass ##prevent the operand from being changed accidentally

def handlerNumbers(event):
    ##Event Handler for number buttons##
    ##Function puts user input in first_num if operand is empty, otherwise input goes second_num##
    global first_num
    global second_num
    global operand

    caller = event.widget['text'] #get the text value of the button that is passed in to the handler

    if operand == None:
        if first_num == None: #check to see if num is set to None as we cannot append to none - must overwrite
            first_num = caller
            updateDisplay(first_num)
        else:
            first_num = first_num + caller
            updateDisplay(first_num)
    else:
        if second_num == None:
            second_num = caller
            updateDisplay(second_num)
        else:
            second_num = second_num + caller
            updateDisplay(second_num)

def handlerClear(event):
    ##Event handler for C button##
    ##Resets variables and updates the display##
    global first_num
    global second_num
    global operand

    first_num = None
    second_num = None
    operand = None

    updateDisplay(0)


##MAIN BODY CODE STARTS##

    ##setup gobal variables that all functions can access##
first_num = None
second_num = None
operand = None



window = Tk()#create the window#
# Code to add widgets will go here...

##Setup frames##
topframe = Frame(window)
topframe.pack()

bottomframe = Frame(window)
bottomframe.pack(side = BOTTOM)
##setup label to display output in top frame##
outputLbl = Label(topframe, text = "0")
outputLbl.pack()
##setup number buttons in grid layout within bottom frame##
b1 = Button(bottomframe, text='1')
b1.bind("<1>", handlerNumbers)
b1.grid(row=0, column = 0)

b2 = Button(bottomframe, text='2') ## create Button called b2 that is inside the bottom frame and displays the label '2'##
b2.bind("<1>", handlerNumbers) ##on b2, bind the event 'when mouse button 1 is clicked (i.e. left mouse button), call the function named 'handlerNumbers'##
b2.grid(row=0, column = 1) ##place button b2 in a grid within its frame, in 0 down and 1 across##

b3 = Button(bottomframe, text='3')
b3.bind("<1>", handlerNumbers)
b3.grid(row=0, column = 2)

b4 = Button(bottomframe, text='4')
b4.bind("<1>", handlerNumbers)
b4.grid(row=1, column = 0)

b5 = Button(bottomframe, text='5')
b5.bind("<1>", handlerNumbers)
b5.grid(row=1, column = 1)

b6 = Button(bottomframe, text='6')
b6.bind("<1>", handlerNumbers)
b6.grid(row=1, column = 2)

b7 = Button(bottomframe, text='7')
b7.bind("<1>", handlerNumbers)
b7.grid(row=2, column = 0)

b8 = Button(bottomframe, text='8')
b8.bind("<1>", handlerNumbers)
b8.grid(row=2, column = 1)

b9 = Button(bottomframe, text='9')
b9.bind("<1>", handlerNumbers)
b9.grid(row=2, column = 2)

b0 = Button(bottomframe, text='0')
b0.bind("<1>", handlerNumbers)
b0.grid(row=3, column = 1)

bDot = Button(bottomframe, text='.')##decimal point button
bDot.bind("<1>", handlerNumbers)
bDot.grid(row=4, column = 0)

##setup operand buttons##

bPlus = Button(bottomframe, text='+')
bPlus.bind("<1>", handlerOperand)
bPlus.grid(row=4, column = 2)

bMinus = Button(bottomframe, text='-')
bMinus.bind("<1>", handlerOperand)
bMinus.grid(row=4, column = 3)

bDivide = Button(bottomframe, text='/')
bDivide.bind("<1>", handlerOperand)
bDivide.grid(row=5, column = 2)

bMultiply = Button(bottomframe, text='*')
bMultiply.bind("<1>", handlerOperand)
bMultiply.grid(row=5, column = 3)

bEquals = Button(bottomframe, text='=')
bEquals.bind("<1>", handlerEquals)
bEquals.grid(row=6, column=0)

##setup Clear button##

bClear = Button(bottomframe, text='C')
bClear.bind("<1>", handlerClear)
bClear.grid(row=6, column=2)

## Code to add widgets ends. Mainloop keeps program running whilst waiting for user input##
window.mainloop()





