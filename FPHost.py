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


    def start_game(self):
        ## Round 1 of the game

        # This should return: the hands of each player, the trump
        # the cards on the table (currently none), the scores (0s)
        game_state = self.game.get_state()
        
        # Inform players the hands they have and the current trump
        for p in self.players:
            self.server.inform_player(p, 
                    game_state.get_hand(p),
                    game_state.get_score(p),
                    game_state.get_trump(),
                    game_state.get_table() )

        # Ask each player to make a prediction
        predictions = {}
        for p in self.players:
            accepted = False
            prediction = None
            while not accepted:
                prediction = self.server.ask_for_prediction(p)
                accepted = self.game.set_prediction(p, prediction)
                # TODO some procedure is needed in case player is not able 
                # to make acceptable predictions, otherwise the game will 
                # stop in an infinite loop (maybe: penalize invalid choice by
                # a random choice by the host?)
            # assuming prediction was accepted
            self.server.confirm_player(p) # tell player it was accepted
            # inform the other players
            self.server.inform_players(p, prediction)

        # In the first round there is only one trick
        # Ask each player what card they want to play in the trick
        for p in self.players:
            card = None
            accepted = False
            while not accepted:
                card = self.server.ask_for_play(p)
                accepted = self.game.set_play(p, card)
            self.server.inform_players(p, card)
        
        game_state = self.game.get_state()
        print('Round 1 is over: Results:')
        game_state.print_results()
