counter = {}

file = open("namen.txt", "r")

names = file.read().splitlines()

file.close()

for line in names:
	if line not in counter:
		counter[line] = 1
	else:
		counter[line] = counter[line] +1

for count in counter:
	print(count, end=': ')
	print(counter[count])