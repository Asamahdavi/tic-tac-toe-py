import math
import random

class Player: 
    def __init__(self, letter):
        # XO 
        self.letter = letter

    # all plyers got their moves
    def get_move(self, game):
        pass 


class RandComputerPlyer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        pass

class UserPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self,game):
        pass
