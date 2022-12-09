with open("aoc-7.txt") as f:
# with open("aoc-7-test.txt") as f:
	lines = [line.strip() for line in f.readlines()]

	# Create a dictionary for all directories
	# Each directory is modeled as a list of file sizes and a list of directories
	folder = {"files": list(), "subdirs": list()}
	dirs = {"/": folder}

	# Given a directory and a dictionary, as above
	# recursively create the size of the directory
	def compute_size(d, dirs):
		# sum the sizes of the top-level files
		total = sum(dirs[d]["files"])
		# add the size of each subdirectory
		for sd in dirs[d]["subdirs"]:
			total += compute_size(sd, dirs)
		return total

	path = ["/"]
	directory = "/"
	dir_path = "/"
	for line in lines[1:]: # skip the first cd command
		if line.startswith("$"): # parse command
			token, command, *args = line.split(" ")

			if command == "cd":
				# parse directory
				directory = args[0]
				if directory != "..": # skip directory changes
					folder = {"files": list(), "subdirs": list()}
					
					path.append(directory)
					dir_path = '/'.join(path)

					dirs[dir_path] = folder
				else:
					path.pop()
			else: # list command
				continue
		elif line.startswith("d"): # directory
			temp, subdir = line.split(" ")
			subdir_path = "/".join(path + [subdir])
			dirs[dir_path]["subdirs"].append(subdir_path)
		else:
			size, name = line.split(" ")
			size = int(size)
			dirs[dir_path]["files"].append(size)

	total = 0
	candidates = list()
	free_space = 70000000 - compute_size("/", dirs)
	need_to_free = 30000000 - free_space
	print(free_space)
	print(need_to_free)
	for d in dirs.keys():
		s = compute_size(d, dirs)

		if s >= need_to_free:
			candidates.append(s)

		if s <= 100000:
			# print(f"{d}: {s} < 100000")
			total += s
		else:
			# print(f"{d}: {s}")
			pass
	print(total)

	print(candidates)
	print(min(candidates))