import random
import operator
import os

# Constants
ANSWER_COUNT = 4

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

score = 0

'''Clears the console.'''
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

'''Formats a number.'''
def formatNumber(num):
    if num % 1 == 0:
        return str(int(num))
    else:
        return '%.2f' % num

'''Generates a question to be used'''
def generateQuestion():
    while True:
        x = random.randint(0, 11)
        y = random.randint(1, 11)
        op = random.choice(list(ops.keys()))
        if op == '/' and y > x:
            continue
        else:
            answer = ops.get(op)(x, y)
            return (x, y, op, answer)

'''Generates a fake answer based on the real answer.'''
def generateFakeAnswer(answer):
    r = random.randint(-11, 11)
    return answer + r

'''Asks a question.'''
def askQuestion():
    global score
    x, y, op, answer = generateQuestion()

    # Generate a list of potential fake answers
    answerList = {}
    answerLocation = random.randint(1, ANSWER_COUNT)

    for i in range(1, 5):
        if i == answerLocation:
            answerList[i] = answer
        else:
            while True:
                generated = generateFakeAnswer(answer)
                if generated != answer and generated not in answerList:
                    answerList[i] = generated
                    break

    # Format that list of potential fake answers into a string
    answers = ''

    for key in answerList:
        value = answerList.get(key)
        answers += '\n%i) %s' % (key, formatNumber(value))

    # Ask the question
    print("""
What is the correct answer to the following expression? %i %s %i
%s
    """ % (x, op, y, answers))

    # Recieve input and mark the user based on it
    while True:
        try:
            userAnswer = float(input('Which is the correct answer? '))
            if userAnswer == answerLocation:
                print('You got it right!')
                score = score + 1
            else:
                print('You got it wrong!')
            break
        except ValueError:
            print('Your input must be a number!')

# Ask the user how many questions they would like to be asked
while True:
    try:
        howMany = int(input('How many questions would you like to answer? '))
        cls()
        for i in range(howMany):
            askQuestion()
            cls()
        print('Your final score is %i/%i!' % (score, howMany))
        break
    except ValueError:
        print('Your input must be a number!')
