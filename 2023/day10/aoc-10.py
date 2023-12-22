pipes = dict()
pipes["|"] = ["north", "south"]
pipes["-"] = ["east", "west"]
pipes["L"] = ["north", "east"]
pipes["J"] = ["west", "north"]
pipes["7"] = ["west", "south"]
pipes["F"] = ["south", "east"]

def flip_direction(direction):
	directions = ["north", "east", "south", "west"]
	return directions[(directions.index(direction) + 2) % 4]

class Grid:
	def __init__(self, lines):
		self.parse_grid(lines)
		self.steps = 1

	def parse_grid(self, lines):
		self.grid = list()

		self.row, self.col = -1, -1
		for row, line in enumerate(lines):
			if self.row == -1:
				try:
					self.col = line.index("S")
					self.row = row
				except ValueError:
					pass
			self.grid.append(list(line))

	def curr_loc(self):
		return self.row, self.col

	def access(self, row, col):
		return self.grid[row][col]

	def curr_pipe(self):
		return self.grid[self.row][self.col]

	def north(self):
		return self.access(self.row - 1, self.col)

	def east(self):
		return self.access(self.row, self.col + 1)

	def south(self):
		return self.access(self.row + 1, self.col)

	def west(self):
		return self.access(self.row, self.col - 1)

	def go(self, direction):
		match direction:
			case "north":
				self.row -= 1
			case "east":
				self.col += 1
			case "south":
				self.row += 1
			case "west":
				self.col -= 1
			case _:
				pass

	def navigate(self, direction):
		self.go(direction)
		while self.curr_pipe() != "S":
			direction = flip_direction(direction)
			sockets = pipes[self.curr_pipe()]
			reroute = sockets[(sockets.index(direction) + 1) % 2]
			self.go(reroute)
			direction = reroute
			self.steps += 1

	def render(self):
		for row in self.grid:
			for col in row:
				print(col, end="")
			print()

with open("aoc-10.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

	grid = Grid(lines)
	
	grid.render()

	print(grid.curr_loc())


	# Preferentially go NESW
	# Check North
	if grid.north() in ["|", "7", "F"]:
		direction = "north"
	# Check East
	elif grid.east() in ["-", "7", "J"]:
		direction = "east"
	# Check West
	elif grid.west() in ["-", "F", "L"]:
		direction = "west"
	# Check South
	elif grid.south() in ["|", "J", "L"]:
		direction = "south"
	else:
		pass

	grid.navigate(direction)
	print(grid.steps)
	print(int(grid.steps/2))
