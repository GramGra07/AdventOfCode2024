fileName = "day3_1.txt"
file = open(fileName, "r")
lines = []
for line in file.readlines():
    lines.append(line)
file.close()

count = 0
toAdd = []
for line in lines:
    line.find('mul')
    clean = line.split('mul(')
    print(clean)
    for i in range(len(clean)):
        clean2 = clean[i].split(')')
        print(clean2)
        for j in range(len(clean2)):
            if clean2[j].count(',') ==1:
                t = clean2[j].split(',')
                try:
                    t[0] = int(t[0])
                    t[1] = int(t[1])
                except:
                    continue
                toAdd.append(t[0]*t[1])
                print(toAdd)


print(sum(toAdd))