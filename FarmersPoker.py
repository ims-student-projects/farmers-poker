from random import shuffle

class Game:
	def __init__(self, players):
		#players: a list of playernumbers (integers)
		assert len(players) == 3
		self.players = {}
		for p in players:
			self.players[p]=(Player(p))
		shuffle(self.players)
		self.suits = ["hearts", "diamonds", "spades", "clubs"]
		self.mkDeck()
		self.state = GameState(self)
		self.maxRounds = 10
		self.round_num = 0
		self.startBasicRound()
		
	"""def startRealGame(self, players):
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
		"""

	def mkDeck(self):
		self.deck=[]
		if len(self.players) == 4:
			for suit in self.suits:
				for value in range(7,15):
					self.deck.append(Card(value, suit))
		else:
			for suit in self.suits:
				for value in range(8,15):
					self.deck.append(Card(value, suit))
			self.deck.append(Card(7, "hearts"))
			self.deck.append(Card(7, "spades"))

	"""def startRound(self):
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
		"""
			
	def startBasicRound(self):
		assert self.round_num < self.maxRounds
		self.round_num += 1
		self.table = []
		shuffle(self.deck)
		self.dealBasicCards()
		self.pickTrump()

	"""def dealCards(self):
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
		"""
				
	def dealBasicCards(self):
		for p in self.players:
			p.hand.append(self.deck[0])
			self.deck.remove(self.deck[0])
		assert self.deck == []

	def pickTrump(self):
		shuffle(self.suits)
		self.trump = self.suits[0]
		self.state.trump = self.trump

	def get_state(self):
		return self.state

	def set_predictions(self, pdict):
		for player, prediction in pdict.items():
			players[player].prediction = prediction

	def set_prediction(self, p, prediction):
		if prediction >= 0 and prediction <=10:
			p.prediction = prediction
			return True
		else:
			return False

	def set_play(self, p, card_played):
		if table:
			if card_played.suit != table[0].suit:
				for card_in_hand in players[p].hand:
					if card_in_hand.suit == table[0].suit:
						return False
		card_played.owner = p
		table.append(card_played)
		players[p].hand.remove(card_played)
		if len(table) == len(players):
			self.trick_collected()
		return True
		
	def trick_collected(self):
		winners = [self.table[0]]
		if self.table[0].suit != self.trump:
			for card in self.table:
				if card.suit == self.trump:
					if winners = [self.table[0]]:
						self.table.remove(self.table[0])
					winners.append = card
		else:
			for card in self.table:
				if card.suit == self.table[0].suit:
					winners.append = card
		highest = 0
		while len(winners)>1:
			for card in winners:
				if card.value >= highest:
					highest = card.value
				else:
					winners.remove[card]
		players[winners[0].owner].tricks.append(self.table)
		if players[0].hand =[]:
			self.end_round()

	def end_round(self):
		for player in players:
			Player.score(player)
		self.get_state()
		self.mkDeck()
		self.state = GameState(self)
		self.startBasicRound()

class Player:
	def __init__(self, p):
		self.hand = []
		self.tricks = []
		self.prediction = None
		self.score = 0

	def score(self):
		if len(self.tricks) == self.prediction:
			self.score += self.prediction*3+10
		else:
			self.score -= 3*(abs(self.prediction-len(self.tricks)))

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		self.owner = None

	def __str__(self):
		return self.suit + str(self.value)

class GameState:
	def __init__(self, game):
		self.players = game.players
		self.trump = None
		self.table = []

	def get_hand(self, player):
		return self.players[player].hand

	def get_tricks(self, player):
		return self.players[player].tricks

	def get_score(self, player):
		return self.players[player].score

	def get_trump(self):
		return self.trump

	def get_table(self):
		return self.table

	def print_results(self):
		print('PLAYER:\tHAND\tTRICKS\tSCORE')
		for p in self.players:
			print('{name}\t{hand}\t{tricks}\t{score}'.format(name = p.name, \
                hand = [c.__str__() for c in p.hand],
                tricks = p.tricks,
                score = p.score ))
			print('TABLE: {}'.format(self.table))
			print('TRUMP: {}'.format(self.trump))
