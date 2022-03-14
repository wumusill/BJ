# 양 끝은 바로 위에 것을 더하고 나머지는 왼쪽 대각선, 오른쪽 대각선 중 큰 것을 더하여 누적

import sys

n = int(sys.stdin.readline())

triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
triangle.sort(key=lambda x: len(x))

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i]) - 1:
            triangle[i][j] += triangle[i - 1][-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[-1]))