import random
from FarmersPoker import Card

class NPServer():

    def start(self):
        players = {'john': '', 'jessie': '', 'liza': ''}
        return players

    def confirm_players(self):
        pass

    def confirm_player(player):
        pass

    def inform_player(player, *state):
        pass

    def inform_players(player, prediction):
        pass


    def ask_for_prediction(player):
        return random.randint()

    def ask_for_play(player):
        suites = ["hearts", "diamonds", "spades", "clubs"]
        card = Card(random.choice(suites), random.randint(7.14))
        return card
