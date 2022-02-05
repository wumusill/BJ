import sys

n, k = map(int, sys.stdin.readline().split())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))

start = 1
end = max(l)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in l:
        total += x // mid

    if total < k:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)