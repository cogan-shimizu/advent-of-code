with open("aoc-8.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

	dirs = lines[0]

	def parse(line):
		node, adjs = line.split(" = ")

		L, R = adjs[1:-1].split(", ")

		return node, L, R

	# Process Nodes
	nodes = dict()
	for line in lines[2:]:
		node, L, R = parse(line)
		nodes[node] = {"L": L, "R": R}

	curr_node = "AAA"
	steps = 0

	while curr_node != "ZZZ":
		curr_dir = dirs[steps % len(dirs)]
		curr_node = nodes[curr_node][curr_dir]
		steps += 1
	print(steps)