import sys
from collections import deque

n = int(sys.stdin.readline().strip())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = int(1e9)

visited = [[True for _ in range(n)] for _ in range(n)]
coasts = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 같은 섬을 1이 아닌 다른 번호로 라벨링 해주기 위한 BFS
island = 1
for a in range(n):
    for b in range(n):
        if mat[a][b] == 1 and visited[a][b]:
            visited[a][b] = False
            mat[a][b] = island
            q = deque([(a, b)])

            while q:
                x, y = q.popleft()
                is_coast = False

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    if mat[nx][ny] == 0:
                        is_coast = True

                    if visited[nx][ny] and mat[nx][ny] != 0:
                        visited[nx][ny] = False
                        mat[nx][ny] = island
                        q.append((nx, ny))

                if is_coast:
                    coasts.append((x, y, island))

            island += 1

is_num = [[0 for _ in range(n)] for _ in range(n)]
dist = [[-1 for _ in range(n)] for _ in range(n)]
q = deque()

for x, y, num in coasts:
    is_num[x][y] = num
    dist[x][y] = 0
    q.append((x, y))

answer = int(1e9)

while q:
    x, y = q.popleft()

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:

            # 바다면 다리 놓기
            if mat[nx][ny] == 0:
                if dist[nx][ny] == -1:                                  # 방문한적 없다면
                    dist[nx][ny] = dist[x][y] + 1                       # 방문 처리
                    is_num[nx][ny] = is_num[x][y]                       # 다녀간 섬 번호 기록
                    q.append((nx, ny))
                elif is_num[nx][ny] != is_num[x][y]:                    # 섬 번호가 다르다 -> 이미 다른 섬의 다리가 있음
                    answer = min(answer, dist[nx][ny] + dist[x][y])     # 거리 더 짧은걸로 갱신

            # 다른 섬 육지 도착하면 거리 갱신
            elif mat[nx][ny] != is_num[x][y]:
                answer = min(answer, dist[x][y])

print(answer)