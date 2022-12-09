with open("aoc-6.txt") as f:
# with open("aoc-6-test.txt") as f:
	signal = f.readlines()[0][:-1]

	print(signal)

	start_packet_length = 14
	count = 0
	for i, marker in enumerate(signal):
		# Skip the first three attempts
		if i < start_packet_length:
			count += 1
			continue

		window = signal[i-start_packet_length:i]
		if len(window) != len(set(window)):
			count += 1
		else:
			break
	print(count)