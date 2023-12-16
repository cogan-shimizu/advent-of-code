with open("aoc-1.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

	cal = 0
	for line in lines:
		nums = list(filter(lambda c : c.isdigit(), line))
		temp = int(nums[0]) * 10 + int(nums[-1])
		cal += temp
	print(cal)