import sys

nums = [0] * 10
n = list(map(int, list(sys.stdin.readline().strip())))

for num in n:
    if num == 6 or num == 9:
        if nums[6] < nums[9]:
            nums[6] += 1
        else:
            nums[9] += 1
    else:
        nums[num] += 1

print(max(nums))