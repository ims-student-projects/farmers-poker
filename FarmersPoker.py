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
		self.d = {"Jack":11, "Queen":12, "King":13, "Ace":14, "7":7, "8":8, "9":9, "10":10}
		self.rev_d = {11:"Jack", 12:"Queen", 13:"King", 14:"Ace", 7:"7", 8:"8", 9:"9", 10:"10"}
		self.mkDeck()
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
		print(self.players[0].name + ", please make a prediction")
			
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
		for p in self.players:
			for card in p.hand:
				p.hand_Verbose.append((self.rev_d[card.value],card.suit))
		for p in self.players:
			print(p.name + "'s hand:")
			print(p.hand_Verbose)
			print("\n")
			
	def pickTrump(self):
		shuffle(self.suits)
		self.trump = self.suits[0]
		print(self.trump + " is the trump")
		print("\n")
			
class Player:
	def __init__(self, p):
		self.name = p
		self.hand = []
		self.hand_Verbose = []

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
