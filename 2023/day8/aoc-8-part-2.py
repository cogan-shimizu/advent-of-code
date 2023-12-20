import math

with open("aoc-8.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

	dirs = lines[0]

	def parse(line):
		node, adjs = line.split(" = ")
		label = node[-1]
		L, R = adjs[1:-1].split(", ")

		return label, node , L, R

	# Process Nodes
	nodes = dict()
	start_nodes = list()
	for line in lines[2:]:
		label, node, L, R = parse(line)
		nodes[node] = {"L": L, "R": R}
		if label == "A":
			start_nodes.append(node)

	cycles = list()
	for curr_node in start_nodes:
		steps = 0
		while curr_node[-1] != "Z":
			curr_dir = dirs[steps % len(dirs)]
			curr_node = nodes[curr_node][curr_dir]
			steps += 1
		cycles.append(steps)
	print(math.lcm(*cycles))