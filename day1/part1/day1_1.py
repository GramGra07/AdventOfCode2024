fileName = "day1_1.txt"
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
difs = []
for i in range(len(right_line)):
    if int(right_line[i])>int(left_line[i]):
        difs.append(int(right_line[i])-int(left_line[i]))
    else:
        difs.append(int(left_line[i])-int(right_line[i]))

print(difs)
print(sum(difs))