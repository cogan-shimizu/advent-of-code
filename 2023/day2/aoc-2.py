# R, G, B
query = (12, 13, 14)

def convert(p):
	return (p["red"], p["green"], p["blue"])

def ispossible(p, q=query):
	for x,y in zip(p,q):
		if x > y:
			return False
	return True

with open("aoc-2.txt", "r") as f:
	s = 0
	for line in f.readlines():
		# process game into structured data
		lhs, rhs = line.strip().split(":")
		# get the game id
		game_id = int(lhs.split(" ")[1])
		# process the pulls
		pulls = rhs.split(";")
		possible = True
		for pull_s in pulls:
			pull = {"red": 0, "green": 0, "blue": 0}
			# marble counts
			counts = pull_s.split(",")
			for count in counts:
				count = count.strip()
				n, c = count.split(" ")
				pull[c] = int(n)

			possible = ispossible(convert(pull))
			if not possible:
				break
		if possible:
			s += game_id
	print(s)

		