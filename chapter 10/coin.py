import random
class coin:
    def __init__(self):
        self.__sideup = 'heads'
    def toss(self):
        if random.randent(0,1) == 0:
            self.__sideup = 'heads'
        else:
            self.__sideup = 'tails'
    def get_sideup(self):
        return self.__sideup