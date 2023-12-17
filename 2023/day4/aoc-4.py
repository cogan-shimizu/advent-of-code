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

	total = 0
	for line in lines:
		card, numbers = line.split(":")
		lhs, rhs = numbers.split("|")
		lhs = re.sub(" +"," ", lhs.strip())
		rhs = re.sub(" +"," ", rhs.strip())

		winning = to_set(lhs.strip())
		have = to_set(rhs.strip())

		points = 2 ** (len(winning.intersection(have)) - 1)
		if points >= 1:
			total += points
	print(total)
