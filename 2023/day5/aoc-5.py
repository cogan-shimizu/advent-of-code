seqs = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

with open("aoc-5.txt") as f:
	lines = f.readlines()

	seeds = lines[0].strip()
	seeds = seeds.split(": ")[1].split(" ")
	seeds = map(int, seeds)

	partition = dict()
	for line in lines[2:]:
		line = line.strip()
		if line == "\n" or line == "":
			continue
		elif not line[0].isdigit():
			name = line.split("-")[2].split(" ")[0]
		else:
			try:
				partition[name] += [line]
			except KeyError:
				partition[name] = [line]

	# for seed in seeds:

	def map_sort(mapping):
		tar, src, rng = map(int, mapping.split(" "))
		return src

	def map_val(val, map_name):
		mappings = sorted(partition[map_name], key=map_sort)

		for mapping in mappings:
			tar, src, rng = map(int, mapping.split(" "))
			if val < src:
				return val
			elif val <= src + rng:
				return tar + (val - src)
			else:
				continue
		return val

	def sow(seed):
		val = seed
		curr = "seed"
		for seq in seqs:
			mapped = map_val(val, seq)
			# print(f"{curr}: {val} -> {seq}: {mapped}")
			val = mapped
		return val # location

	print(min(map(sow, seeds)))
