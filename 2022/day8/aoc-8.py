import operator
from functools import reduce

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
	# Collector for view distances
	view_distances = list()
	# Iterate
	count = 0
	for row_num, row_data in enumerate(grid_rows):
		# Consider only interior trees
		if row_num == 0 or row_num == len(grid_rows) - 1:
			continue

		for col_num, tree_height in enumerate(row_data):
			# Consider only interior trees 
			if col_num == 0 or col_num == len(row_data) - 1:
				continue

			# Define a function that computes the view_distance
			# for this particular tree height:
			def calc_view_distance(trees):
				vd = 0
				for tree in trees:
					# count the current tree
					vd += 1
					# halt on trees equal to or greater than
					if tree >= tree_height:
						return vd
				# return length of the list
				return vd
			# Get tree heights in each direction
			left, right = split_list(row_data, col_num)
			left.reverse() # order matters for part 2
			col_data = grid_cols[col_num]
			top, bottom = split_list(col_data, row_num)
			top.reverse() # order matters for part 2

			# Check for visibility in each direction
			# Only visibility in one direction is necessary
			directions = [left, right, top, bottom]
			# commented out for part 2
			# for direction in directions:
			# 	if max(direction) < tree_height:
			# 		interior += 1
			# 		break

			# part 2
			# map the view distance of each direction to an integer
			# create a list, and reduce (i.e., find the product of all elements)
			# collect it in view_distances
			product = reduce(operator.mul, list(map(calc_view_distance, directions)), 1)
			view_distances.append(product)
			count += 1

	# Output results
	max_view_distance = max(view_distances)
	print(f"max_view_distance: {max_view_distance}")
	# print(f"exterior: {exterior}")
	# print(f"interior: {interior}")
	# print(f"     sum: {exterior + interior}")