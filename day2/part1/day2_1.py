fileName = "day2_1.txt"
file = open(fileName, "r")
lines = []
for line in file.readlines():
    lines.append(line)
file.close()

count = 0

for line in lines:
    count1 = 0
    last = 0
    increase = 0
    split = line.split(' ')
    new=[]
    for line in split:
        new.append(line.replace('\n',''))
    nums = []
    for i in new:
        nums.append( int(i.replace('\n','')))
    shouldIncrease = 0
    print(nums)
    last = nums[0]
    if (last-nums[1]>0):
        shouldIncrease = 0
    else:
        shouldIncrease = 1

    for i in range(len(nums)):
        if shouldIncrease ==1:
            dif = nums[i]-last
            if (dif>0 and dif<=3):
                count1+=1
        else:
            dif = last-nums[i]
            if (dif >0 and dif<=3):
                count1+=1

        last = nums[i]
    if (count1 == len(nums)-1):
        count+=1


print(count)