with open("aoc-9.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

	predictions = list()
	for line in lines:
		values = [int(token) for token in line.split(" ")]

		lsts = [values]
		while not all(map(lambda x: x == 0, values)):
			tmp = list()
			for x,y in zip(values[:-1], values[1:]):
				d = y - x
				tmp.append(d)
			values = tmp
			lsts.append(tmp)
		s = 0
		for lst in reversed(lsts):
			s += lst[-1]
		predictions.append(s)
	print(sum(predictions))