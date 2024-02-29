# python3 시간 초과, pypy3 통과
import sys
from collections import deque


def solution(x, y, k, visited):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    # k : 벽을 깰 수 있는 횟수
    q = deque([[x, y, k]])
    visited[x][y][k] = 1

    # visited[nx][ny][벽을 깰 수 있는 기회] 에 거리 기록
    while q:
        x, y, t = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][t]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽을 깰 기회가 남았다면 꺠고 visited[nx][ny][t - 1] 에 거리 기록
            if t > 0 and graph[nx][ny] == 1 and visited[nx][ny][t - 1] == 0:
                visited[nx][ny][t - 1] = visited[x][y][t] + 1
                q.append([nx, ny, t - 1])
            # 벽이랑 상관 없이 갈 수 있는 길이라면 거리 기록
            elif graph[nx][ny] == 0 and visited[nx][ny][t] == 0:
                visited[nx][ny][t] = visited[x][y][t] + 1
                q.append([nx, ny, t])

    return -1


n, m, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
print(solution(0, 0, k, visited))