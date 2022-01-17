# 메모리 초과
n = int(input())
array = [int(input()) for _ in range(n)]
cnt = [0] * (max(array) + 1)

for i in array:
    cnt[i] += 1

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i)

# 메모리 초과
n = int(input())
array = [int(input()) for _ in range(n)]
cnt = []
already = []

for i in array:
    if i in already:
        continue
    else:
        cnt.append((i, array.count(i)))
        already.append(i)

cnt.sort(key=lambda x:x[0])

for num, times in cnt:
    for _ in range(times):
        print(num)

####################################################################
import sys
n = int(sys.stdin.readline())
cnt = [0] * 10001

for _ in range(n):
    cnt[int(sys.stdin.readline())] += 1

for i in range(10001):
    if cnt[i] != 0:
        for j in range(cnt[i]):
            print(i)