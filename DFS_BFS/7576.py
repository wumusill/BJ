from collections import deque

queue = deque([])
graph = []
n, m = map(int, input().split())
for i in range(m):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            queue.append([i, j])


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

bfs()

num_1 = []
num_m1 = []
max_l = []
l_0 = []
for i in graph:
    num_1.append(i.count(1))
    num_m1.append(i.count(-1))
    l_0.append(i.count(0))
    max_l.append(max(i))
if sum(num_1) + sum(num_m1) == n * m:
    print(0)
elif sum(l_0) >= 1:
    print(-1)
else:
    print(max(max_l)-1)
    
###################################################
res = 0
for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            break
    res = max(res, max(i))
print(res - 1)