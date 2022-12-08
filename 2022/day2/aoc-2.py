with open("aoc-2.txt") as f:
	lines = f.readlines()

	total = 0
	
	def shape_points(shape):
		if shape == "A": # or shape == "X":
			return 1
		elif shape == "B": # or shape == "Y":
			return 2
		else:
			return 3

	def eval_move(move):
		their_move, result = move.strip().split(" ")
		
		winning_move = ((shape_points(their_move) + 0) % 3) + 1
		losing_move  = ((shape_points(their_move) + 1) % 3) + 1

		

		# ((shape_points(their_move) + 0) % 3) + 1

		# X -> lose
		if result == "X":
			return 0 + losing_move
		# Y -> draw
		if result == "Y":
			return 3 + shape_points(their_move)
		# Z -> lose
		if result == "Z":
			return 6 + winning_move
		
		

	# 	# win
	# 	if their_move == "A" and your_move == "Y":
	# 		return 6 + shape_points(your_move)
	# 	if their_move == "B" and your_move == "Z":
	# 		return 6 + shape_points(your_move)
	# 	if their_move == "C" and your_move == "X":
	# 		return 6 + shape_points(your_move)

	# 	# lose
	# 	if their_move == "A" and your_move == "Z":
	# 		return shape_points(your_move)
	# 	if their_move == "B" and your_move == "X":
	# 		return shape_points(your_move)
	# 	if their_move == "C" and your_move == "Y":
	# 		return shape_points(your_move)

	# 	# draw
	# 	if shape_points(their_move) == shape_points(your_move):
	# 		return 3 + shape_points(your_move)
	# print(list(map(eval_move, lines)))
	total = sum(map(eval_move, lines))
	print(total)