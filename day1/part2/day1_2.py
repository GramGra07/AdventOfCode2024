fileName = "day1_2.txt"
file = open(fileName, "r")
lines = []
for line in file.readlines():
    lines.append(line)
file.close()

left_line = []
right_line = []

for line in lines:
    split = line.split('   ')
    left_line.append(split[0])
    right_line.append(split[1].replace('\n',''))

right_line.sort()
left_line.sort()

counts = []

for line in left_line:
    n = line
    counts.append(int(n)*right_line.count(n))
print(sum(counts))