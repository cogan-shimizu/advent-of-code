from random import shuffle
import sys

def translate(symbol):
	try:
		i = ["A", "K", "Q", "J", "T"].index(symbol)
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

		if any(map(lambda x : x == 4, cards.values())):
			self.category = 2
			return

		if 3 in cards.values():
			if 2 in cards.values():
				self.category = 3
			else:
				self.category = 4
			return

		counter = 0
		for count in cards.values():
			if count == 2:
				counter += 1
		if counter == 2:
			self.category = 5
		elif counter == 1:
			self.category = 6
		else:
			self.category = 7

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
	hands.sort()

	for hand in hands:
		print(hand)
	print()

	winnings = 0
	for rank, hand in enumerate(reversed(hands)):
		rank += 1
		score = rank * hand.bid
		winnings += score
	print(winnings)

