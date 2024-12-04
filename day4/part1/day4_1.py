fileName = "day4_1.txt"
file = open(fileName, "r")
lines = []
for line in file.readlines():
    lines.append(line.strip())
file.close()

count = 0
for l in range(len(lines)):
    line = lines[l]
    for i in range(len(line)):
        if line[i] == 'X':
            # Check right
            if i + 3 < len(line) and line[i+1] == 'M' and line[i+2] == 'A' and line[i+3] == 'S':
                count += 1
            # Check left
            if i - 3 >= 0 and line[i-1] == 'M' and line[i-2] == 'A' and line[i-3] == 'S':
                count += 1
            # Check down
            if l + 3 < len(lines) and lines[l+1][i] == 'M' and lines[l+2][i] == 'A' and lines[l+3][i] == 'S':
                count += 1
            # Check up
            if l - 3 >= 0 and lines[l-1][i] == 'M' and lines[l-2][i] == 'A' and lines[l-3][i] == 'S':
                count += 1
            # Check down-right diagonal
            if l + 3 < len(lines) and i + 3 < len(line) and lines[l+1][i+1] == 'M' and lines[l+2][i+2] == 'A' and lines[l+3][i+3] == 'S':
                count += 1
            # Check up-left diagonal
            if l - 3 >= 0 and i - 3 >= 0 and lines[l-1][i-1] == 'M' and lines[l-2][i-2] == 'A' and lines[l-3][i-3] == 'S':
                count += 1
            # Check down-left diagonal
            if l + 3 < len(lines) and i - 3 >= 0 and lines[l+1][i-1] == 'M' and lines[l+2][i-2] == 'A' and lines[l+3][i-3] == 'S':
                count += 1
            # Check up-right diagonal
            if l - 3 >= 0 and i + 3 < len(line) and lines[l-1][i+1] == 'M' and lines[l-2][i+2] == 'A' and lines[l-3][i+3] == 'S':
                count += 1

print(count)