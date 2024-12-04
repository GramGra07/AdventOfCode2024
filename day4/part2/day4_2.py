fileName = "day4_2.txt"
file = open(fileName, "r")
lines = []
for line in file.readlines():
    lines.append(line.strip())
file.close()

count = 0

for l in range(len(lines)):
    line = lines[l]
    for i in range(len(line)):
        if line[i] == 'A':
            if l - 1 >= 0 and l + 1 < len(lines) and i - 1 >= 0 and i + 1 < len(line):
                if (lines[l-1][i-1] == 'M' and lines[l+1][i+1] == 'S' and
                    lines[l-1][i+1] == 'S' and lines[l+1][i-1] == 'M'):
                    count += 1
                if (lines[l-1][i-1] == 'S' and lines[l+1][i+1] == 'M' and
                    lines[l-1][i+1] == 'M' and lines[l+1][i-1] == 'S'):
                    count += 1
                if (lines[l-1][i-1] == 'M' and lines[l+1][i+1] == 'S' and
                    lines[l-1][i+1] == 'M' and lines[l+1][i-1] == 'S'):
                    count += 1
                if (lines[l-1][i-1] == 'S' and lines[l+1][i+1] == 'M' and
                    lines[l-1][i+1] == 'S' and lines[l+1][i-1] == 'M'):
                    count += 1

print(count)