from FPServer import FPServer
from FarmersPoker import Game

class FPHost():

    def __init__(self):
        self.server = FPServer()
        # Wait until server gets three players registered
        self.players = self.server.start(3)
        self.game = Game(self.players.keys())
        # Inform players that they're accepted to the game
        self.server.confirm_players()
        self.start_game()


    def start_game():
        ## Round 1 of the game

        # This should return: the hands of each player, the trump
        # the cards on the table (currently none), the scores (0s)
        game_state = self.game.get_state()
        
        # Inform players the hands they have and the current trump
        for p in self.players:
            self.server.inform_player(p, 
                    game_state.get_hand(p),
                    game_state.get_score(p),
                    game_state.get_trump,
                    game_state_get_table)


        # Ask each player to make a prediction
        predictions = {}
        for p in self.players:
            predictions[p] = self.server.ask_for_prediction(p)
            # Inform other players
            self.server.inform_players(p, predictions[p])
        # Inform Game
        self.game.set_predictions(predictions)
