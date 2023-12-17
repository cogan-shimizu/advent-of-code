import re
import operator
from functools import reduce

def to_set(s):
	tokens = s.split(" ")
	tokens_mapped = map(int, tokens)
	token_set = set(tokens_mapped)
	return token_set

with open("aoc-4.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

	counters = dict()
	for i in range(1,len(lines)+1):
		counters[i] = 1

	for curr, line in enumerate(lines):
		# parsing
		card, numbers = line.split(":")
		card = re.sub(" +", " ", card)
		card_num = int(card.split(" ")[1])
		lhs, rhs = numbers.split("|")
		lhs = re.sub(" +"," ", lhs.strip())
		rhs = re.sub(" +"," ", rhs.strip())
		winning = to_set(lhs.strip())
		have = to_set(rhs.strip())

		# 1-indexing
		curr += 1

		num_matches = len(winning.intersection(have))
		for i in range(counters[curr]):
			for j in range(1, num_matches + 1):
				counters[curr + j] += 1

	total = 0
	for i in range(1, len(lines) + 1):
		total += counters[i]
	print(total)