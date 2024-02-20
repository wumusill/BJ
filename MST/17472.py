import sys
from collections import deque


def make_island(stack, name):
    '''섬에 이름을 붙여주는 함수'''
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while stack:
        x, y = stack.pop()
        matrix[x][y] = name
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] and visited[nx][ny]:
                visited[nx][ny] = False
                stack.append((nx, ny))


def search_bridge(q):
    '''서로 다른 섬 사이에 건설할 수 있는 다리를 찾는 함수'''
    direction = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
    visited = [[True for _ in range(m)] for _ in range(n)]
    while q:
        x, y, d, l = q.popleft()

        if d == 's':                                            # 처음엔 사방위의 바다 존재를 파악
            start = matrix[x][y]
            for t in direction:
                nx, ny = x + direction[t][0], y + direction[t][1]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] and matrix[nx][ny] == 0:
                    visited[nx][ny] = False                     # 바다를 만나면 다리의 방향과 함께 좌표 기록
                    q.append((nx, ny, t, 1))

        else:                                                   # 처음이 아니라면
            nx, ny = x + direction[d][0], y + direction[d][1]   # 기존에 짓던 다리의 방향으로 계속 건설
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if matrix[nx][ny] and l > 1:                        # 길이가 2 이상이면서 섬에 도달 했으면
                bridges.append([start, matrix[nx][ny], l])      # [출발 섬, 도착섬, 다리 길이] 기록
            if visited[nx][ny] and not matrix[nx][ny]:
                visited[nx][ny] = False
                q.append((nx, ny, d, l + 1))


def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[True for _ in range(m)] for _ in range(n)]

# 섬마다 이름을 붙임
name = 1
for a in range(n):
    for b in range(m):
        if matrix[a][b] and visited[a][b]:
            make_island([(a, b)], name)
            name += 1

# 서로 다른 섬 사이에 건설할 수 있는 다리를 찾음
bridges = []
for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            search_bridge(deque([(i, j, 's', 0)]))

# 다리 길이 순으로 오름차순 정렬
# 모든 다리를 연결해도 모든 섬이 연결되지 않을 수 있음
# 이를 파악하기 위해 다리의 개수도 기록
# 다리의 개수가 (섬의 개수 - 1)이 아니라면 모든 섬이 연결된 것이 아님
parent = [i for i in range(name)]
bridges.sort(key=lambda x: x[2])
bridge_cnt, answer = 0, 0

# 크루스칼 알고리즘 시행
for a, b, c in bridges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += c
        bridge_cnt += 1

if answer == 0 or bridge_cnt != name - 2:
    print(-1)
else:
    print(answer)

# 10 6
# 0 0 0 1 0 0
# 0 0 0 1 0 0
# 0 1 0 0 0 1
# 0 0 0 0 0 0
# 1 1 0 1 1 0
# 1 0 0 0 1 0
# 1 1 0 0 1 0
# 0 0 0 0 1 1
# 0 0 0 0 0 0
# 0 1 0 0 0 0
# 13