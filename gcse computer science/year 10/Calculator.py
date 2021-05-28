operators=["+","-", "*", "/"] #list of operators
operatorNames=["add","subtract","multiply","divide"]

def addNums(num1, num2):
    """Function to return to sum of the parameters"""
    answer = num1+num2
    return answer

def subNums(num1,num2):
    answer = num1-num2
    return answer

def multiplyNums(num1,num2):
    answer = num1*num2
    return answer

def divideNums(num1,num2):
    answer = num1/num2
    return answer

def checkChoice():
    global operators
    choice = (input("Enter the operator"))
    if choice in operators:
        return choice

    else:
        print("Error!")
        return ""
        #end of choice check
def menu():
    """Subroutine to run the menu"""
    global operators # global variable to access the list of operators
    global operatorNames # global variable to access the list of operator names
    choice = "" #declare an empty string variable to hold the user's choice of operator
    answer = 0 #declare an integer variable to hold the result
    number1 = int(input("Enter Number 1"))
    number2 = int(input("Enter Number 2"))
    #-----------------print the accepted operators--------------------
    print ("Select the operator:")
    for i in range(0,len(operators)):
        print(operators[i]," ", operatorNames[i])
    #-----------------call the checkChoice function--------------------
    while choice=="":
        choice = checkChoice()
    #-----------------call the correct operator function--------------------
    if choice == "+":
        answer = addNums(number1,number2)
    elif choice =="-":
        answer = subNums(number1,number2)
    elif choice == "*":
        answer = multiplyNums(number1,number2)
    elif choice == "/":
        if number2 == 0:
            print('You can not divide by zero!')
            menu()
        else:
            answer = divideNums(number1,number2)
    else:
        print("sorry something went wrong!")
    #-----------------output--------------------
    print(number1, choice, number2, "=", answer)
    return

menu()






