with open("aoc-8.txt") as f:
# with open("aoc-8-test.txt") as f:
	# Ingest and clean
	lines = [line.strip() for line in f.readlines()]

	# Prepare data "model"
	grid_rows = list()
	grid_cols = list()
	ncols = len(lines[0])
	for i in range(ncols):
		grid_cols += [list()]

	# "Model" the data
	for line in lines:
		row = [int(d) for d in line]
		grid_rows += [row]

		for d, col in zip(row, grid_cols):
			col.append(d)

	# split the list over the provided index (exclusive)
	def split_list(lst, index):
		left = lst[:index]
		right = lst[index+1:]
		return (left, right)

	# Initially count exterior
	exterior = 2 * (len(grid_rows) + len(grid_cols) - 2)
	# Collector for the interior
	interior = 0
	# Iterate
	for row_num, row_data in enumerate(grid_rows):
		# Consider only interior trees
		if row_num == 0 or row_num == len(grid_rows) - 1:
			continue

		for col_num, tree_height in enumerate(row_data):
			# Consider only interior trees 
			if col_num == 0 or col_num == len(row_data) - 1:
				continue


			# Get tree heights in each direction
			left, right = split_list(row_data, col_num)
			col_data = grid_cols[col_num]
			top, bottom = split_list(col_data, row_num)

			# Check for visibility in each direction
			# Only visibility in one direction is necessary
			for direction in [left, right, top, bottom]:
				if max(direction) < tree_height:
					interior += 1
					break

	# Output results
	print(f"exterior: {exterior}")
	print(f"interior: {interior}")
	print(f"     sum: {exterior + interior}")