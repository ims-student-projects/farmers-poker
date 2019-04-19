from FPServer import FPServer
from FarmersPoker import Game

class FPHost():

    def __init__(self):
        self.server = FPServer()
        # Wait until server enough players registered
        self.players = self.server.start()
        self.game = Game(self.players.keys())
