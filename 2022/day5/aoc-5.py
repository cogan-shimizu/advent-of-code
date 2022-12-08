# with open("aoc-5.txt") as f:
with open("aoc-5-test.txt") as f:
	lines = [line[:-1] for line in f.readlines()]

	stack_rows = list()
	nl = 0
	for nl, line in enumerate(lines):
		if line != "":
			blanked_row = line.replace(" [", "-[")
			blanked_row = blanked_row.replace("] ", "]-")
			blanked_row = blanked_row.replace("   ", "[0]")
			stack_rows += [blanked_row]
		else:
			break
	stack_rows = stack_rows[:-1]
	# print(f"nl: {nl}")
	cols = len(lines[nl-1][1:-1].split("   "))
	# print(f"cols: {cols}")

	stack_rows = reversed(stack_rows)

	stacks = [list() for c in range(cols)]
	for row in stack_rows:
		blocks = row.split("-")
		for i, block in enumerate(blocks):
			if block != "[0]":
				stacks[i].append(block)

	for line in lines[nl+1:]:
		pass