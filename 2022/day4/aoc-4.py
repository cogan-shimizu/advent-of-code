with open("aoc-4.txt") as f:
	lines = [line.strip() for line in f.readlines()]

	def get_sections(bounds):
		lower, upper = bounds.split("-")
		lower = int(lower)
		upper = int(upper)
		section_range = range(lower,upper+1)
		sections = list(section_range)

		return set(sections)

	count = 0
	for line in lines:
		left_elf, right_elf = line.split(",")

		sections = [get_sections(left_elf), get_sections(right_elf)]
		overlap = set.intersection(*sections)

		# if overlap in sections:
		if len(overlap) > 0:
			count += 1
	print(count)