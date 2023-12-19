from random import shuffle
import sys

def translate(symbol):
	if symbol == "J":
		return 1
	try:
		i = ["A", "K", "Q", "T"].index(symbol)
		val = 14 - i
		return val
	except ValueError:
		return int(symbol)

class Hand:
	def __init__(self, hand, bid):
		self.hand = hand
		self.bid = bid

		self.categorize()

	def categorize(self):
		self.category = 1

		if self.hand[0] * 5 == self.hand:
			self.category = 1
			return

		cards = dict()
		for card in self.hand:
			try:
				cards[card] += 1
			except KeyError:
				cards[card] = 1

		jokers = 0
		try:
			jokers = cards["J"]
		except KeyError:
			pass

		joker = jokers > 0

		if jokers == 4:
			self.category = 1 # five of a kind
		elif jokers == 3:
			if 2 in cards.values():
				self.category = 1 # five of a kind
			else:
				self.category = 2 # four of a kind
			return
		elif jokers == 2:
			if 3 in cards.values():
				self.category = 1 # five of a kind
			else:
				counter = 0
				for card in cards.values():
					if card == 2:
						counter += 1
				if counter == 2:
					self.category = 2 # four of a kind
				else:
					self.category = 4 # three of a kind
			return
		elif jokers == 1:
			pass # this will be taken care of later
		else:
			pass # continue scoring as normal

		if any(map(lambda x : x == 4, cards.values())):
			if joker:
				self.category = 1 # five of a kind
			else:
				self.category = 2 # four of a kind
			return

		if 3 in cards.values():
			if 2 in cards.values():
				self.category = 3 # full house
			else:
				if joker:
					self.category = 2 # four of a kind
				else:
					self.category = 4 # three of a kind
			return

		counter = 0
		for count in cards.values():
			if count == 2:
				counter += 1
		if counter == 2:
			if joker:
				self.category = 3 # full house
			else:
				self.category = 5 # two pair
		elif counter == 1:
			if joker:
				self.category = 4 # three of a kind
			else:
				self.category = 6 # pair
		else:
			if joker:
				self.category = 6 # pair
			else:
				self.category = 7 # high card

	def __lt__(self, other):
		if self.category == other.category:
			for s, o in zip(self.hand, other.hand):
				if translate(s) == translate(o):
					continue
				else:
					return translate(s) > translate(o)
		else:
			return self.category < other.category

	def __str__(self):
		return f"{self.hand} ({self.category}) : {self.bid}"

with open("aoc-7.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

	hands = list()
	for line in lines:
		hand, bid = line.strip().split(" ")
		bid = int(bid)

		hands.append(Hand(hand, bid))
	hands.sort(reverse=True)

	for hand in hands:
		print(hand.hand)
	print()

	winnings = 0
	for rank, hand in enumerate(hands, start=1):
		score = rank * hand.bid
		winnings += score
	print(winnings)