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
				
	def deal(self, num_hands, num_cards):
		hands = []
		for hand in range(num_hands):
			hands.append(Hand([]))
		if num_cards == -1:
			card_count = 0
			while len(self.cards) != 0:
				hands[card_count % num_hands].add_card(self.pop_card())
				card_count += 1
			return hands
		for cycle in range(num_cards):
			for hand in hands:
				hand.add_card(self.pop_card())
		return hands


class Hand():

    def __init__(self, init_cards):
        self.cards = init_cards

    def add_card(self, card):
        card_strs = [] 
        for c in self.cards: 
            card_strs.append(c.__str__()) 
        if card.__str__() not in card_strs: 
            self.cards.append(card) 

    def remove_card(self, card):
        x = [c.__str__() for c in self.cards]
        card_hand = str(card)
        if card_hand in x:
            index = x.index(card_hand)
            del self.cards[index]
            return card 

    def draw(self, deck):
        self.add_card(deck.pop_card())
 
class Game():
	
