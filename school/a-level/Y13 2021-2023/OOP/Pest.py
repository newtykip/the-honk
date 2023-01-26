class Pest:
    def __init__(self, legs, noise):
        self.__legs = legs
        self.__noise = noise

    def getLegs(self):
        return self.__legs

    def getNoise(self):
        return self.__noise

dog = Pest(4, 'woof')
roach = Pest(6, 'click click click')

print(roach.getNoise())