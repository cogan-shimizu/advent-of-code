num_pairs = [("one", "1"),
("two", "2"),
("three", "3"),
("four", "4"),
("five", "5"),
("six", "6"),
("seven", "7"),
("eight", "8"),
("nine", "9")]

def reverse_string(s):
	return s[::-1]

def iter_replace(s):
	left, right = "", ""
	for i in range(len(s)):
		if s[i].isdigit():
			left = s[i]
		else:
			for ns, nd in num_pairs:
				if s[i:i+len(ns)] == ns:
					left = nd
					break
		if left != "":
			break
	s = reverse_string(s)
	for i in range(len(s)):
		if s[i].isdigit():
			right = s[i]
		else:
			for ns, nd in num_pairs:
				nsr = reverse_string(ns)
				if s[i:i+len(nsr)] == nsr:
					right = nd
		if right != "":
			break
	return(left, right)

with open("aoc-1.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

	cal = 0
	for line in lines:
		line = iter_replace(line)
		num = int(''.join(line))
		cal += num
	print(cal)