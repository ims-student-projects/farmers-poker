import random
from FarmersPoker import Card

class FPServer():

    def start(self, count=3):
        players = {'john': '', 'jessie': '', 'liza': ''}
        return players

    def confirm_players(self):
        pass

    def confirm_player(self, player):
        pass

    def inform_player(self, player, *state):
        pass

    def inform_players(self, player, prediction):
        pass


    def ask_for_prediction(self, player):
        return random.randint(0, 1)

    def ask_for_play(self, player):
        suites = ["hearts", "diamonds", "spades", "clubs"]
        card = Card(random.choice(suites), random.randint(7, 14))
        return card
