import sys
from collections import deque

queue = deque()
queue_RG = deque()
n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip('\n')) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
visited_RG = [[False] * n for _ in range(n)]
ans = 0
ans_RG = 0
color = graph[0][0]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            queue.append((i, j))
            color = graph[i][j]
            ans += 1
        while queue:
            x, y = queue.popleft()
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for t in range(4):
                nx = x + dx[t]
                ny = y + dy[t]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if visited[nx][ny] == False and graph[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        if visited_RG[i][j] == False:
            queue_RG.append((i, j))
            color = graph[i][j]
            ans_RG += 1
        while queue_RG:
            x, y = queue_RG.popleft()
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for t in range(4):
                nx = x + dx[t]
                ny = y + dy[t]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if color == 'B':
                    if visited_RG[nx][ny] == False and graph[nx][ny] == color:
                        visited_RG[nx][ny] = True
                        queue_RG.append((nx, ny))
                else:
                    if visited_RG[nx][ny] == False and graph[nx][ny] in ['R', 'G']:
                        visited_RG[nx][ny] = True
                        queue_RG.append((nx, ny))

print(ans, ans_RG)