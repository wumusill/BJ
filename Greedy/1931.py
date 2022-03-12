import sys

ans = 0
n = int(sys.stdin.readline())

time_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
time_list.sort(key=lambda x:(x[1], x))

pre_start, pre_end = time_list[0][0], time_list[0][1]
for i in range(1, n):
    new_start = time_list[i][0]
    new_end = time_list[i][1]
    if pre_end <= new_start:
        ans += 1
        pre_end = new_end

print(ans + 1)