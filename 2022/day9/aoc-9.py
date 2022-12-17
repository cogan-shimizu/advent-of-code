class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __hash__(self):
		return hash((self.x, self.y))

	def __eq__(self, other):
		if not isinstance(other, type(self)): return NotImplemented
		return self.x == other.x and self.y == other.y 

	def __add__(self, other):
		return Position(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		return Position(self.x - other.x, self.y - other.y)

	def __str__(self):
		return f"Position({self.x},{self.y})"

	def distance(self, other):
		dx = abs(self.x - other.x)
		dy = abs(self.y - other.y)

		return max(dx, dy)

	def move_direction(self, direction):
		if d == "R":
			dir_movement = Position(1, 0)
		elif d == "L":
			dir_movement = Position(-1, 0)
		elif d == "U":
			dir_movement = Position(0, 1)
		else: # d == "D":
			dir_movement = Position(0, -1)

		return self + dir_movement

with open("aoc-9.txt") as f:
	# Ingest
	lines = [line.strip() for line in f.readlines()]

	def move_tail(head, tail):
		distance = head.distance(tail)
		# Only move if we have to
		if distance < 2:
			return tail

		# Determine the direction to move the tail
		difference = head - tail
		if difference == Position(2,0): # head is right
			new_tail = tail.move_direction("R")
		elif difference == Position(-2,0): # head is left
			new_tail = tail.move_direction("L")
		elif difference == Position(0,2): # head is above
			new_tail = tail.move_direction("U")
		elif difference == Position(0,-2): # head is below
			new_tail = tail.move_direction("D")
		elif difference == Position(1,2): # right 1 and up 2
			new_tail = tail + Position(1,1)
		elif difference == Position(2,1): # up 1 and right 2
			new_tail = tail + Position(1,1)
		elif difference == Position(-1,2): # left 1 and up 2
			new_tail = tail + Position(-1,1)
		elif difference == Position(-2,1): # left 2 and up 1
			new_tail = tail + Position(-1,1)
		elif difference == Position(1,-2): # right 1 and down 2
			new_tail = tail + Position(1,-1)
		elif difference == Position(2,-1): # right 2 and down 1
			new_tail = tail + Position(1,-1)
		elif difference == Position(-2,-1): # left and down
			new_tail = tail + Position(-1,-1)
		elif difference == Position(-1,-2): # left and down
			new_tail = tail + Position(-1,-1)
		else:
			return NotImplemented

		return new_tail

	# Initial locations
	curr_head_pos = Position(0,0)
	curr_tail_pos = Position(0,0)
	# Collectors for positions
	head_positions = set()
	tail_positions = set()
	head_positions.add(curr_head_pos)
	tail_positions.add(curr_tail_pos)

	# Process instructions
	for line in lines:
		d, n = line.split(" ")

		for i in range(int(n)):
			curr_head_pos = curr_head_pos.move_direction(d)
			head_positions.add(curr_head_pos)

			curr_tail_pos = move_tail(curr_head_pos, curr_tail_pos)
			tail_positions.add(curr_tail_pos)

	print(f"Unique head positions: {len(head_positions)}")
	print(f"Unique tail positions: {len(tail_positions)}")