import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().rstrip().split()))
l.sort()

answer = []

start, end = 0, n - 1

while start < end:
    answer.append([l[start], l[end], abs(l[start] + l[end])])
    if abs(l[start]) < abs(l[end]):
        end -= 1
    else:
        start += 1

answer.sort(key=lambda x: x[2])

print(answer[0][0], answer[0][1])