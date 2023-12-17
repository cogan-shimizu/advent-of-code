from functools import reduce
import operator

def convert(p):
	return [p["red"], p["green"], p["blue"]]

def maxes(mins, pull):
	return [max(m,p) for m, p in zip(mins, pull)]

with open("aoc-2.txt", "r") as f:
	s = 0
	for line in f.readlines():
		# process game into structured data
		lhs, rhs = line.strip().split(":")
		# get the game id
		game_id = int(lhs.split(" ")[1])
		# process the pulls
		pulls = rhs.split(";")
		mins = [0, 0, 0]		
		for pull_s in pulls:
			pull = {"red": 0, "green": 0, "blue": 0}
			# marble counts
			counts = pull_s.split(",")
			for count in counts:
				count = count.strip()
				n, c = count.split(" ")
				pull[c] = int(n)
			mins = maxes(mins,convert(pull))
		power = reduce(operator.mul, mins)
		s += power
	print(s)
		