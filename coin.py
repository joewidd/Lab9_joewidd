"""
Matching Coin Game,
Joe Widdifield,
Create a coin matching game between 2 players,
9/22/2026
"""
import random

class Coin:
    def __init__(self):
        self.__sideup = ""
        self.toss()

    def toss(self):
        if random.randrange(0, 2) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup
