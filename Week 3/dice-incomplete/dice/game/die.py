import random


# TODO: Implement the Die class as follows...


class Die:
    def __init__(self):
        self.value = 0
        self.points = 0
    def roll(self):
        self.value = random.randint(1, 6)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0

