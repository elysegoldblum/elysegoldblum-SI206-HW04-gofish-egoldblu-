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
	
	#Hand 1's turn
	if hand_num == 1:
		count = 0
		#Check to see if input equals a cards rank in hand 2's list of cards.
		#If yes, remove the card and add it to hand 1.
		#Update count so player 1 will be able to go again.
		for x in h2.cards:
			if int(value_input) == x.rank_num:
				print(x.rank_num)
				h2.remove_card(x)
				h1.add_card(x)
				count +=1

			#Print the respective hands for each player.
			#Continue at the end allows for player 1 to go again.
		if count != 0:
			print("Hand 1")
			h1_ranks = []
			h2_ranks = []
			for x in h1.cards:
				h1_ranks.append(x.rank)
			print(h1_ranks)
			print()

			print("Hand 2")
			for x in h2.cards:

				h2_ranks.append(x.rank)
			print(h2_ranks)
			hand_num = 1
			continue

			#Have player 1 draw a card from the deck.
			#Print respective hands for each player and now it's player 2's turn.
		else:
			h1.draw(d)

			print("Hand 1")
			h1_ranks = []
			h2_ranks = []
			for x in h1.cards:
				h1_ranks.append(x.rank)
			print(h1_ranks)
			print()

			print("Hand 2")
			for x in h2.cards:
				h2_ranks.append(x.rank)
			print(h2_ranks)

			hand_num = 2
	else:

		count = 0
		#Check to see if input equals a cards rank in hand 1's list of cards.
		#If yes, remove the card and add it to hand 2.
		#Update count so player 2 will be able to go again.
		for x in h1.cards:
			if int(value_input) == x.rank_num:
				h1.remove_card(x)
				h2.add_card(x)
				count +=1

		#Print the respective hands for each player.
		#Continue at the end allows for player 2 to go again.
		if count != 0:
			print("Hand 1")
			h1_ranks = []
			h2_ranks = []
			for x in h1.cards:
				h1_ranks.append(x.rank)
			print(h1_ranks)
			print()

			print("Hand 2")
			for x in h2.cards:
				h2_ranks.append(x.rank)
			print(h2_ranks)
			hand_num = 2
			continue

		#Have player 2 draw a card from the deck.
		#Print respective hands for each player and now it's player 1's turn.
		else:
			h2.draw(d)
			print("Hand 1")
			h1_ranks = []
			h2_ranks = []
			for x in h1.cards:
				h1_ranks.append(x.rank)
			print(h1_ranks)
			print()

			print("Hand 2")
			for x in h2.cards:
				h2_ranks.append(x.rank)
			print(h2_ranks)
			hand_num = 1
