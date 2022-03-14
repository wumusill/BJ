# 각 라인의 처음과 끝은 바로 위에 숫자를 더해주면 되고, 나머지는 왼쪽 대각선, 오른쪽 대각선 중 최댓값을 더해나가 계속 누적시키면 됨


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