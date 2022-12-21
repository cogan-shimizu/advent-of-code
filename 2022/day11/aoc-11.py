class Monkey:
	def __init__(self, chunk):
		self.num_inspections = 0
		# Store only the number RHS - ":"
		self.name = chunk[0].split(" ")[1][:-1]
		# Parse the items
		self.parse_items(chunk[1])
		self.operation = Operation(chunk[2])
		self.parse_test(chunk[3:])

	def __str__(self):
		mstr = f"Monkey {self.name}:\n"
		mstr += f"\tStarting items: {self.items}\n"
		mstr += f"\tOperation: {self.operation}\n"
		mstr += f"\tTest: {self.test}\n"
		return mstr

	def parse_items(self, item_str):
		items_list = item_str.split(": ")[1]
		items = items_list.split(", ")
		self.items = list()
		for item in items:
			self.items.append(int(item))

	def parse_test(self, test_chunk):
		divisor = test_chunk[0].split(" ")[-1]
		divisor = int(divisor)
		# Only interested in the monkey label
		true_case = test_chunk[1].split(" ")[-1]
		false_case = test_chunk[2].split(" ")[-1]
		self.test = Test(divisor, true_case, false_case)

	def do_turn(self, monkeys):
		for item in self.items:
			# Calculate new worry
			value = self.operation.execute(item)
			# Monkey got bored
			value = int(value / 3)
			# Do test
			target = self.test.execute(value)
			# Throw to next monkey
			monkeys[target].items.append(value)
			# Increment
			self.num_inspections += 1
		# All items have been thrown
		self.items = list()

class Operation:
	def __init__(self, op_str):
		formula = op_str.split("= ")[-1]
		self.lhs, self.op, self.rhs = formula.split(" ")

	def __str__(self):
		ostr = f"new = {self.lhs} {self.op} {self.rhs}"
		return ostr

	def execute(self, worry):
		lhs = self.lhs
		if lhs == "old":
			lhs = worry
		else:
			lhs = int(lhs)

		rhs = self.rhs
		if rhs == "old":
			rhs = worry
		else:
			rhs = int(rhs)

		if self.op == "+":
			value = lhs + rhs
		elif self.op == "-":
			value = lhs - rhs
		elif self.op == "*":
			value = lhs * rhs
		elif self.op == "/":
			value = lhs / rhs
		else:
			return NotImplemented

		return value

class Test:
	def __init__(self, divisor, tc, fc):
		self.divisor = divisor
		self.tc = tc
		self.fc = fc

	def __str__(self):
		tstr = f"divisible by {self.divisor}\n"
		tstr += f"\t\tIf true: throw to monkey {self.tc}\n"
		tstr += f"\t\tIf false: throw to monkey {self.fc}"
		return tstr

	def execute(self, value):
		if value % self.divisor == 0:
			return self.tc
		else:
			return self.fc

with open("aoc-11.txt") as f:
	# Ingest and clean
	lines = [line.strip() for line in f.readlines()]
	# Collector
	monkeys = dict()
	# Process
	prev = 0
	count = 0
	for interval in range(7,len(lines)+7,7):
		# Capture
		monkey_raw = lines[prev:interval]
		prev = interval
		# Process
		monkey = Monkey(monkey_raw)
		print(monkey)
		monkeys[str(count)] = monkey
		count += 1

	# Do 20 rounds
	for round_num in range(20):
		for key in monkeys.keys():
			monkey = monkeys[key]
			monkey.do_turn(monkeys)
	# Determine monkey business
	inspections = list()
	for key in monkeys.keys():
		monkey = monkeys[key]
		inspections.append(monkey.num_inspections)
	x,y = sorted(inspections, reverse = True)[:2]
	monkey_business = x * y
	print(monkey_business)