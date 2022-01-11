import random

class EightBall:
    def __init__(self):
        self.responses = ['It is certain.','It is decidedly so.','Without a doubt.','Yes — definitely.','You may rely on it.','As I see it, yes.','Most likely.','Outlook good.','Yes.','Signs point to yes.','Reply hazy, try again.','Ask again later.','Better not tell you now.','Cannot predict now.','Concentrate and ask again.','Don’t count on it.','My reply is no.','My sources say no.','Outlook not so good.','Very doubtful.']
    def answer(self):
        return random.choice(self.responses)

ball = EightBall()
question = input('What is your question for the magic 8 ball?')

print("""
Q: %s
A: %s
""" % (question, ball.answer()))