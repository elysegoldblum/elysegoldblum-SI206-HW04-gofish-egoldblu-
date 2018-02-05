import random


class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces:
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)


class Hand():
	def __init__(self, cards=[]):
		self.cards = cards

	def add_card(self, card):
		self.cards.append(card)

	def draw(self, deck):
		self.add_card(deck.pop_card())

	def remove_card(self,card):

		self.cards.remove(card)

class Deck(object):
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		return "\n".join(total)

	def remove_card(self, card= Card()):
		self.cards.remove(card)

	def pop_card(self):
		return self.cards.pop()

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = []
		for c in self.cards:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			self.cards.append(card)

	def sort_cards(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

	def deal(self):
		hand = []
		for card in self.cards:
			if len(hand) < 7:
				x = random.choice(self.cards)
				hand.append(x)
				self.remove_card(x)

		return hand
	
d = Deck()
h1 = Hand(cards = d.deal())
h2 = Hand(cards = d.deal())

hand_num = 1
while len(d.cards) != 0:
	if len(h1.cards) == 0:
	print("Player 2 wins")
	break
elif len(h2.cards) == 0:
	print("Player 1 wins")
	break
else:
	print()
	print("Hand {}'s turn".format(hand_num))
	value_input = input("Enter value between 1 and 13 (1=Ace,above 10 are face cards in ascending order): ")
