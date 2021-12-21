import uuid
import os
import re

name = input('Please input your name!')
score = 0

def question1(score):
    answer = int(input('What is 5 times 5?'))

    if answer == 25:
        score = score + 1

    question2(score)

def question2(score):
    answer = int(input('What is 12 times 12?'))

    if answer == 144:
        score = score + 1

    question3(score)

def question3(score):
    answer = int(input('What is 3 cubed?'))

    if answer == 27:
        score = score + 1

    save(score)

def save(score):
    f = open('quizresult-' + str(uuid.uuid1()) + '.txt', 'x')
    f.write('Name: ' + name)
    f.write('\nQuiz result: ' + str(score) + '/3')
    f.close()

    leaderboard()


# todo: sort out leaderboard by score
def leaderboard():
    for filename in os.listdir('/'):
        if (filename.endswith('.txt') == True) & (filename.find('quizresult-') != -1):
            f = open(filename)

            contents = f.read()
            score = re.search('./3', contents).group().split('/')[0]

            print(contents + '\n')

question1(score)