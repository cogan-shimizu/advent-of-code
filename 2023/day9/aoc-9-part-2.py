with open("aoc-9.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

	predictions = list()
	for line in lines:
		values = [int(token) for token in line.split(" ")]

		starts = [values[0]]
		while not all(map(lambda x: x == 0, values)):
			tmp = list()
			for x,y in zip(values[:-1], values[1:]):
				d = y - x
				tmp.append(d)
			values = tmp
			starts.append(tmp[0])
		s = 0
		starts.reverse()

		d = 0
		for i in starts:
			d = i - d

		predictions.append(d)
	print("====")
	print(sum(predictions))