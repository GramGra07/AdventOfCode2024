fileName = "day2_2.txt"
lines = []

with open(fileName, "r") as file:
    lines = file.readlines()

def is_safe(nums):
    shouldIncrease = nums[0] <= nums[1]
    last = nums[0]
    for i in range(1, len(nums)):
        if shouldIncrease:
            if not (0 < nums[i] - last <= 3):
                return False
        else:
            if not (0 > nums[i] - last >= -3):
                return False
        last = nums[i]
    return True

count = 0

for line in lines:
    nums = [int(num) for num in line.split()]
    if is_safe(nums):
        count += 1
    else:
        for i in range(len(nums)):
            if is_safe(nums[:i] + nums[i+1:]):
                count += 1
                break

print(count)