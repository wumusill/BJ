import sys
import heapq


n, m = map(int, sys.stdin.readline().strip().split())
mat = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(m)]
visited = [[1e9 for _ in range(n)] for _ in range(m)]
q = []

heapq.heappush(q, (mat[0][0], 0, 0))
visited[0][0] = mat[0][0]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    c, x, y = heapq.heappop(q)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        cost = c + mat[nx][ny]
        if cost < visited[nx][ny]:
            visited[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

print(visited[-1][-1])