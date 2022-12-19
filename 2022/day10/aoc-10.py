class Device:
	def __init__(self):
		self.register = 1
		self.cycle = 1
		self.signal_strength = 0

	def tick(self):
		self.cycle += 1
		if (self.cycle - 20) % 40 == 0:
			ss = self.cycle * self.register
			print(ss)
			self.signal_strength += ss

	def do_inst(self, inst, *values):
		if inst == "noop":
			self.tick()
		elif inst == "addx":
			v = int(values[0])
			self.tick()
			self.register += v
			self.tick()

with open("aoc-10.txt") as f:
	lines = [line.strip() for line in f.readlines()]

	device = Device()
	for line in lines:
		device.do_inst(*line.split(" "))

	print(device.signal_strength)