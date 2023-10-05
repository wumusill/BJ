import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[True for _ in range(m)] for _ in range(n)]
ans = [0, 0]


def bfs(x, y):
    global ans, visited, mat
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()

    q.append((x, y))
    size = 1
    visited[x][y] = False
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny] and mat[nx][ny] == 1:
                visited[nx][ny] = False
                q.append((nx, ny))
                size += 1

    ans[1] = max(ans[1], size)


for x in range(n):
    for y in range(m):
        if visited[x][y] and mat[x][y] == 1:
            ans[0] += 1
            bfs(x, y)

print(ans[0])
print(ans[1])