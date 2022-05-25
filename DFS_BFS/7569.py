import sys
from collections import deque

queue = deque()
n, m, h = map(int, sys.stdin.readline().split())
visited = [[False] * n for _ in range(m * h)]
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(m * h)]

for i in range(m * h):
    for j in range(n):
        if tomato[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            queue.append((i, j))
while queue:
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -m, m]
    nx, ny = queue.popleft()
    for k in range(6):
        x = nx + dx[k]
        y = ny + dy[k]
        z = nx + dz[k]
        if x < 0 or y < 0 or z < 0 or y >= n or x >= (m * h) or z >= (m * h):
            continue
        if k == 0 and x % m == (m - 1):
            continue
        elif k == 1 and x % m == 0:
            continue
        if k < 4:
            if tomato[x][y] == 0 and visited[x][y] == False:
                tomato[x][y] = tomato[nx][ny] + 1
                visited[x][y] = True
                queue.append((x, y))
        else:
            if tomato[z][y] == 0 and visited[z][y] == False:
                tomato[z][y] = tomato[nx][ny] + 1
                visited[z][y] = True
                queue.append((z, y))

ans = 0
for i in range(m * h):
    if 0 in tomato[i]:
        ans = 0
        break
    else:
        ans = max(ans, max(tomato[i]))

print(ans - 1)