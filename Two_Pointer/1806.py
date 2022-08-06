import sys

n, s = map(int, sys.stdin.readline().rstrip().split())
l = list(map(int, sys.stdin.readline().rstrip().split()))

answer = int(1e9)
start, end = 0, 0
res = l[0]

while True:
    if res >= s:
        answer = min(answer, end - start + 1)
        res -= l[start]
        start += 1
    else:
        end += 1
        if end == n:
            break
        res += l[end]


print(answer if answer != int(1e9) else 0)