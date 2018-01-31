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
	def __init__(self,init_cards):
		self.cards = init_cards
	def add_card(self, card):
		card_strs = []
		for c in self.cards:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			self.cards.append(card)
	def remove_card(self, card):
		card_string = []
		for card in self.cards:
			card_string.append(card.__str__())
		new_card = str(card)
		if new_card in card_string:
			place = card_string.index(new_card)
			del self.cards[place]
			return card
	def draw(self, deck):
		self.add_card(deck.pop_card())
	def remove_pairs(self):
		ranks = {}
		for card in self.cards:
			if card.rank in ranks:
				ranks[card.rank].append(card)
			else:
				ranks[card.rank] = [card]
		final_cards = []
		for rank in ranks.values():
			card_to_remove = len(rank) % 2
			if card_to_remove == 1:
				final_cards.append(rank[-1])
		self.cards = final_cards


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

	def pop_card(self, i=-1):
		return self.cards.pop(i) 
	def shuffle(self):
		random.shuffle(self.cards)

	def sort_cards(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)
				
	def deal(self, num_hands=2, num_cards=7):
		h1 = Hand()
		h2 = Hand()
		hands = [h1, h2]
		for hand in range(num_hands):
			for cycle in range(num_cards):
				hands[hand].add_card(self.pop_card())
		return hands
	
d = Deck()
print (
h1 = d.deal()[0]
h2 = d.deal()[1]
	

value_input = input("‘Please choose a card rank you would like to ask the other player if they have (between 1-13):")
if value_input  h1.cards:
	in
	

