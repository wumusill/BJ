import sys

n = int(sys.stdin.readline())
num_List = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())
ans = 0

start = 0
end = n - 1

while start < end:
    _sum = num_List[start] + num_List[end]
    if _sum == x:
        ans += 1
        end -= 1
    elif _sum < x:
        start += 1
    else:
        end -= 1

print(ans)