# python3 시간 초과, pypy3 통과
# import sys
# from collections import deque
#
# n, m = map(int, sys.stdin.readline().split())
# graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
#
#
# def bfs(i, j, res):
#     visited = [[True for _ in range(m)] for _ in range(n)]
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     q = deque()
#     cnt = 0
#
#     if visited[i][j]:
#         q.append((i, j, res))
#         visited[i][j] = False
#         while q:
#             x, y, dist = q.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                     continue
#                 if visited[nx][ny] and graph[nx][ny] == 'L':
#                     visited[nx][ny] = False
#                     q.append((nx, ny, dist + 1))
#                     cnt = max(cnt, dist + 1)
#
#     return cnt
#
#
# ans = 0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 'L':
#             ans = max(ans, bfs(i, j, 0))
#
# print(ans)
############################################################################
# python3 최적화 된 코드 참고 후 구현했으나 틀림 -> 이후 수정
import sys
from collections import deque


def solution():
    n, m = map(int, sys.stdin.readline().split())
    graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
    visited = [[True for _ in range(m)] for _ in range(n)]

    q = deque()

    # 최장 거리, 최장 거리가 갱신될 때마다 좌표 저장
    dist = 0
    points = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'L' and visited[i][j]:
                visited[i][j] = False
                q.append((i, j, 0))
                while q:
                    x, y, d = q.popleft()

                    # 최장 거리가 등장하면 값 갱신하고 좌표 저장
                    if d > dist:
                        dist = d
                        points.append((x, y))
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if visited[nx][ny] and graph[nx][ny] == 'L':
                            visited[nx][ny] = False
                            q.append((nx, ny, d + 1))

    res = 0
    # 최장 거리 좌표 순회
    # 최장 거리 구하기
    for i, j in points:
        visited = [[True for _ in range(m)] for _ in range(n)]
        visited[i][j] = False
        q.append((i, j, 0))
        while q:
            x, y, d = q.popleft()
            if d > res:
                res = d
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny] and graph[nx][ny] == 'L':
                    visited[nx][ny] = False
                    q.append((nx, ny, d + 1))

    return res


print(solution())
###########################################################################
def solution():
    L, W = map(int, input().split())
    board = [tuple([*input().rstrip()]) for _ in range(L)]
    visited = [[False] * W for _ in range(L)]
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    points = []
    dist = 0
    for i in range(L):
        for j in range(W):
            if board[i][j] == 'L' and not visited[i][j]:
                visited[i][j] = True
                queue = [(i, j, 0)]
                while queue:
                    r, c, d = queue.pop(0)
                    if d > dist:
                        dist = d
                        points.append((r, c))
                    for dr, dc in delta:
                        nr, nc = r + dr, c + dc
                        if L > nr >= 0 and W > nc >= 0:
                            if board[nr][nc] == 'L' and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc, d + 1))
    res = 0
    for i, j in points:
        visited = [[False] * W for _ in range(L)]
        visited[i][j] = True
        queue = [(i, j, 0)]
        while queue:
            r, c, d = queue.pop(0)
            if d > res:
                res = d
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if L > nr >= 0 and W > nc >= 0:
                    if board[nr][nc] == 'L' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc, d + 1))
    print(res)


solution()