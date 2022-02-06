import sys

n ,m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

result = 0
start = 0
end = max(l)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in l:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)