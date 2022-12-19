class Device:
	def __init__(self):
		self.register = 1
		self.cycle = 1
		self.col = 0

	def tick(self):
		self.draw()
		self.cycle += 1
		self.col += 1

	def draw(self):
		# Draw a new line (if not the first time)
		if self.col != 0:
			self.col %= 40
			if self.col == 0:
				print()

		# Detect sprite
		if self.col == self.register - 1:
			print("#", end="")
		elif self.col == self.register:
			print("#", end="")
		elif self.col == self.register + 1:
			print("#", end="")
		else:
			print(".", end="")

	def do_inst(self, inst, *values):
		if inst == "noop":
			self.tick()
		elif inst == "addx":
			v = int(values[0])
			self.tick()
			# self.register += v
			self.tick()
			self.register += v

with open("aoc-10.txt") as f:
	lines = [line.strip() for line in f.readlines()]

	device = Device()
	for line in lines:
		device.do_inst(*line.split(" "))