import sys
from collections import deque

n = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().strip().split())


def bfs(n, r1, c1, r2, c2):
    mat = [[-1 for _ in range(n)] for _ in range(n)]
    dx = [-2, -2, 0, 0, 2, 2]
    dy = [-1, 1, -2, 2, -1, 1]
    q = deque()
    q.append((r1, c1))
    mat[r1][c1] = 0
    while q:
        x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if mat[nx][ny] == -1:
                mat[nx][ny] = mat[x][y] + 1
                q.append((nx, ny))

    return mat[r2][c2]


print(bfs(n, r1, c1, r2, c2))