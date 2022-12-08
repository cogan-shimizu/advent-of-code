with open("aoc-1.txt") as f:
	
	total = 0
	totals = list()
	for line in f.readlines():
		if line == "\n":
			totals.append(total)
			total = 0
		else:
			total += int(line.strip())
	print(sorted(totals)[-3:])
	print(sum(sorted(totals)[-3:]))