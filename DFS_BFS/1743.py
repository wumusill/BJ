import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().strip().split())
mat = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(k):
    r, c = map(int, sys.stdin.readline().strip().split())
    mat[r - 1][c - 1] = 1


# 연결된 음식물의 개수를 bfs를 이용하여 return하는 함수
def bfs(a, b):
    global visited
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    res = 0
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if mat[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                res += 1
    return res


# matrix 순회하면서 bfs 함수 실행
ans = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1 and visited[i][j] == False:
            # 더 큰 값으로 갱신
            ans = max(ans, bfs(i, j))

print(ans)