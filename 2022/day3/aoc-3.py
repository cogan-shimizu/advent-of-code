with open("aoc-3.txt") as f:
	lines = f.readlines()

	def assign_priority(item):
		temp = item.lower()

		v = ord(temp) + 1 - ord("a")

		if item.isupper():
			return v + 26
		else:
			return v

	# def process(line):
	# 	line = line.strip()
	# 	l = len(line)
	# 	m = int(l / 2)
		
	# 	items = list(line)
	# 	first = set(items[:m])
	# 	second = set(items[m:])

	# 	common = first.intersection(second)
	# 	item = list(common)[0]
	# 	return assign_priority(item)

	# print(sum(map(process, lines)))

	total = 0
	prev = 0
	for i in range(2, len(lines), 3):
		group = lines[prev:i+1]
		bags = [set(list(bag.strip())) for bag in group]
		badge = set.intersection(*bags)

		total += assign_priority(list(badge)[0])

		prev = i+1
		
	print(total)