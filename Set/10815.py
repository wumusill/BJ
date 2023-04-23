import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
key_list = list(map(int, sys.stdin.readline().split()))

ans_dict = {}

for key in key_list:
    ans_dict[key] = 0

for num in num_list:
    try:
        ans_dict[num] += 1
    except:
        continue

for answer in ans_dict.values():
    print(answer, end=' ')