from random import shuffle

class Game:
	def __init__(self, players):
		#players: a list of playernames (strings)
		assert len(players) == 3 or len(players) == 4
		self.players = []
		for p in players:
			self.players.append(Player(p))
		shuffle(self.players)
		self.suits = ["hearts", "diamonds", "spades", "clubs"]
		self.mkDeck()
		self.state = GameState(self)
		if len(self.players) == 3:
			self.countRounds = 9
		else:
			self.countRounds = 7
		self.maxRounds = self.countRounds + 5 + self.countRounds
		self.round_num = 0
		self.startRound()
		
	def mkDeck(self):
		self.deck=[]
		for suit in self.suits:
			if len(self.players) == 4:
				for value in range(7,15):
					self.deck.append(Card(value, suit))
			else:
				for value in range(8,15):
					self.deck.append(Card(value, suit))
				self.deck.append(Card(7, "hearts"))
				self.deck.append(Card(7, "spades"))
				
	def startRound(self):
		assert self.round_num < self.maxRounds
		self.round_num += 1
		self.table = []
		shuffle(self.deck)
		if self.round_num != self.countRounds + 3:
			self.dealCards()
		if self.round_num == self.countRounds + 1:
			self.trump = "hearts"
		elif self.round_num == self.countRounds + 2:
			self.trump = "spades"
		elif self.round_num == self.countRounds + 4:
			self.trump = "diamonds"
		elif self.round_num == self.countRounds + 5:
			self.trump = "clubs"
		else:
			self.pickTrump()
			
	def dealCards(self):
		if self.round_num <= self.countRounds:
			cardsDealt_num = self.round_num
		elif self.round_num > self.countRounds + 5:
			cardsDealt_num = self.maxRounds + 1 - self.round_num
		else:
			cardsDealt_num = self.countRounds + 1
		for i in range(cardsDealt_num):
			for p in self.players:
				p.hand.append(self.deck[0])
				self.deck.remove(self.deck[0])
			
	def pickTrump(self):
		shuffle(self.suits)
		self.trump = self.suits[0]
		
	def get_state:
		return self.state
			
class Player:
	def __init__(self, p):
		self.name = p
		self.hand = []
		self.tricks = []
		self.score = 0

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

class GameState:
	def __init__(self, game):
		self.players = game.players
		self.trump = None
		self.table = []
	
	def get_hand(player):
		for i in range(len(self.players)):
			if player == self.players[i]:
				return self.players[i].hand
				
	def get_tricks(player):
		for i in range(len(self.players)):
			if player == self.players[i]:
				return self.players[i].tricks
				
	def get_score(player):
		for i in range(len(self.players)):
			if player == self.players[i]:
				return self.players[i].score
				
	def get_trump:
		return self.trump
		
	def get_table:
		return self.table
