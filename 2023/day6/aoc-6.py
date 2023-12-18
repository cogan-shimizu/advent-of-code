import re

def parse(s):
	return list(map(int, re.sub(" +", " ", s.split(":")[1].strip()).split(" ")))

with open("aoc-6.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]


	times = parse(lines[0])
	dists = parse(lines[1])
	print(times)
	print(dists)

	prod = 1
	for time, dist in zip(times, dists):
		counter = 0
		for a in range(time):
			travel = (a * time) - (a ** 2)
			if travel > dist:
				counter += 1
		prod *= counter
	print(prod)