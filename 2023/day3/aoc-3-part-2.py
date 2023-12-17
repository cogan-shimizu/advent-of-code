import re

with open("aoc-3.txt") as f:
	# We leave the newlines in as a "end of line"
	lines = f.readlines()

	# Explode the array
	arr = list()
	for line in lines:
		arr += [[*line]]

	"""
	The overall strategy is to mark numbers with some index value, this prevents us from 
	double counting a single number that is adjacent to a symbol, but catches if two
	identical numbers are adjacent to the same symbol (which is ok)
	"""
	counter = 0
	vals = dict()
	accum = ""
	# Replace single digits with the value of the whole number
	for i, line in enumerate(lines):
		# replace non-periods and non-digits with a space
		# standardize = re.sub("\*", " ", line)
		standardize = re.sub("[^\d\*^\.]", ".", line)
		print(standardize)
		# accumulate 
		accum = ""
		for j, c in enumerate(standardize):
			if c == "." or c == "*" or c == "\n":
				# if c == " ":
				# 	arr[i][j] = " "
				if accum == "":
					continue
				else:
					# When a stop character is detected, replace
					# previous digits with the marking counter
					val = int(accum)
					vals[counter] = val
					for index in range(len(accum),0,-1):
						arr[i][j-index] = counter
					counter += 1
					accum = ""
			else:
				accum += c

	# Uniquely count numbers adjacent to symbols
	total = 0
	for row_in, row in enumerate(arr):
		for col_in, col in enumerate(row):
			if col == "*":
				gear_adjs = set()
				for row_offset in range(-1, 2):
					for col_offset in range(-1, 2):
						row_look = row_in + row_offset
						col_look = col_in + col_offset
						# avoid indexerrors or wrapping
						if row_look < 0 or col_look < 0 or row_look == len(arr) or col_look == len(row):
							continue
						else:
							v = arr[row_look][col_look]
							if isinstance(v, int):
								gear_adjs.add(v)
				if len(gear_adjs) == 2:
					prod = 1
					for v in gear_adjs:
						prod *= vals[v]
					total += prod
	print(total)
