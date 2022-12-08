with open("aoc-6.txt") as f:
# with open("aoc-6-test.txt") as f:
	signal = f.readlines()[0][:-1]

	print(signal)

	count = 0
	for i, marker in enumerate(signal):
		# Skip the first three attempts
		if i < 4:
			count += 1
			continue

		window = signal[i-4:i]
		if len(window) != len(set(window)):
			count += 1
		else:
			break
	print(count)