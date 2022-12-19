class Position:
	def __init__(self, x, y, label = None):
		self.x = x
		self.y = y
		if label == 0:
			label = "H"
		self.label = label

	def __hash__(self):
		return hash((self.x, self.y))

	def __eq__(self, other):
		"""Note that the label is counted at all"""
		if not isinstance(other, type(self)): return NotImplemented
		return self.x == other.x and self.y == other.y 

	def __add__(self, other):
		"""Retain label of LHS"""
		return Position(self.x + other.x, self.y + other.y, self.label)

	def __sub__(self, other):
		"""Retain label of LHS"""
		return Position(self.x - other.x, self.y - other.y, self.label)

	def __str__(self):
		return f"Position({self.x},{self.y})"

	def get_copy(self):
		x = self.x
		y = self.y
		label = self.label

		return Position(x,y,label)

	def touching(self, other):
		dx = abs(self.x - other.x)
		dy = abs(self.y - other.y)

		return dx <= 1 and dy <= 1

	def move_direction(self, direction):
		if direction == "R":
			dir_movement = Position(1, 0)
		elif direction == "L":
			dir_movement = Position(-1, 0)
		elif direction == "U":
			dir_movement = Position(0, 1)
		elif direction == "D":
			dir_movement = Position(0, -1)
		else:
			return NotImplemented			

		return self + dir_movement

	def follow(self, other):
		# Only move if we have to
		if other.touching(self):
			return self

		# Determine the direction to move the self
		difference = other - self
		new_tail = self

		if difference == Position(2,0):     # right 2 and above 0
			new_tail = self.move_direction("R")
		elif difference == Position(-2,0):  # left  2 and above 0
			new_tail = self.move_direction("L")
		elif difference == Position(0,2):   # right 0 and above 2
			new_tail = self.move_direction("U")
		elif difference == Position(0,-2):  # right 0 and below 2
			new_tail = self.move_direction("D")
		elif difference == Position(1,2):   # right 1 and   up  2
			new_tail = self + Position(1,1)
		elif difference == Position(2,1):   # right 2 and   up  1
			new_tail = self + Position(1,1)
		elif difference == Position(-1,2):  # left  1 and   up  2
			new_tail = self + Position(-1,1)
		elif difference == Position(-2,1):  # left  2 and   up  1
			new_tail = self + Position(-1,1)
		elif difference == Position(1,-2):  # right 1 and down  2
			new_tail = self + Position(1,-1)
		elif difference == Position(2,-1):  # right 2 and down  1
			new_tail = self + Position(1,-1)
		elif difference == Position(-2,-1): # left  2 and down  1
			new_tail = self + Position(-1,-1)
		elif difference == Position(-1,-2): # left  1 and down  2
			new_tail = self + Position(-1,-1)
		elif difference == Position(2,2):   # right 2 and   up  2
			new_tail = self + Position(1,1)
		elif difference == Position(-2,2):  # left  2 and   up  2
			new_tail = self + Position(-1,1)
		elif difference == Position(2,-2):  # right 2 and down  2
			new_tail = self + Position(1,-1)
		elif difference == Position(-2,-2): # left  2 and down  2
			new_tail = self + Position(-1,-1)
		else:
			return NotImplemented

		return new_tail

class Rope:
	def __init__(self, length):
		self.knots = list()
		self.length = length
		self.tail_positions = set()

		for i in range(length):
			self.knots.append(Position(0,0,i))

	def __str__(self):
		s = "Rope:\n"
		for i, knot in enumerate(self.knots):
			if i == 0:
				i = "H"
			s += f"\t{i}:" + str(knot) + "\n"
		return s

	def move_head(self, direction):
		# Move the head in the direction
		self.knots[0] = self.knots[0].move_direction(direction)
		# Update the following knots
		# purposefully not using enumerate
		# since we need to one index to skip the head
		for i, knot in zip(range(1,self.length), self.knots[1:]):
			self.knots[i] = knot.follow(self.knots[i-1])
		self.tail_positions.add(self.get_tail())

	def get_head(self):
		return self.knots[0]

	def get_tail(self):
		return self.knots[-1]

	def print_grid(self, h = 21, w = 26, offset = None):
		grid_rows = list()
		for i in range(h):
			cols = list()
			for i in range(w):
				cols.append(".")
			grid_rows.append(cols)

		if offset == None:
			cx = int(w/2)
			cy = int(h/2)
		else:
			cx, cy = offset

		for i, knot in enumerate(self.knots):
			if i == 0:
				i = "H"
			kx = knot.x + cx
			ky = knot.y + cy

			if grid_rows[ky][kx] == ".":
				grid_rows[ky][kx] = str(i)

		if grid_rows[cy][cx] == ".":
			grid_rows[cy][cx] = "s"

		for row in reversed(grid_rows):
		# for row in grid_rows:
			print ("".join(row))
		print()

with open("aoc-9.txt") as f:
	# Ingest
	lines = [line.strip() for line in f.readlines()]

	# Initial locations
	curr_head_pos = Position(0,0)
	curr_tail_pos = Position(0,0)
	# Collectors for positions
	head_positions = set()
	tail_positions = set()
	head_positions.add(curr_head_pos)
	tail_positions.add(curr_tail_pos)

	# A Rope is a list of 10 knots
	rope = Rope(10)
	# Process instructions
	for line in lines:
		d, n = line.split(" ")

		print(f"== {d} {n} ==")
		for i in range(int(n)):
			# curr_head_pos = curr_head_pos.move_direction(d)
			# head_positions.add(curr_head_pos)
			# curr_tail_pos = move_tail(curr_head_pos, curr_tail_pos)
			rope.move_head(d)

	# print(f"Unique head positions: {len(head_positions)}")
	print(f"Unique tail positions: {len(rope.tail_positions)}")