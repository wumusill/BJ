import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
mat = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
ans = [[-1 for _ in range(m)] for _ in range(n)]


def bfs(x, y):
    global ans
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    ans[x][y] = 0
    q.append((x, y, 0))

    while q:
        x, y, res = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if ans[nx][ny] == -1 and mat[nx][ny] != 0:
                ans[nx][ny] = res + 1
                q.append((nx, ny, res + 1))


for i in range(n):
    for j in range(m):
        if mat[i][j] == 2:
            bfs(i, j)
        elif mat[i][j] == 0:
            ans[i][j] = 0

for ans in ans:
    print(*ans)