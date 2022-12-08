with open("aoc-5.txt") as f:
# with open("aoc-5-test.txt") as f:
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

	for stack in stacks:
		print(stack)

	# def move_crates(source, target, num, stacks):
	# 	if num == 0:
	# 		return

	# 	crate = stacks[source].pop()
	# 	stacks[target].append(crate)

	# 	move_crates(source, target, num-1, stacks)
	def move_crates(source, target, num, stacks):
		crates = stacks[source][-num:]
		stacks[source] = stacks[source][:-num]
		stacks[target] += crates

	for line in lines[nl+1:]:
		print(line)
		# parse the code
		move, num, frum, source, to, target = line.split(" ")
		num = int(num)
		source = int(source) - 1 # zero index, one label
		target = int(target) - 1 # zero index, one label

		move_crates(source, target, num, stacks)

	tops = ""
	for stack in stacks:
		if len(stack) > 0:
			top = stack[-1]
			label = top[1:-1]
			tops += label
	print(tops)