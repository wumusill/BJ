import sys
from collections import deque


def solution(a, b, campus, visited):
    result = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([(a, b)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] and campus[nx][ny] != 'X':
                if campus[nx][ny] == 'P':
                    result += 1
                q.append((nx, ny))
                visited[nx][ny] = False

    return result


n, m = map(int, sys.stdin.readline().split())
campus = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[True for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            visited[i][j] = False
            result = solution(i, j, campus, visited)
            print(result if result > 0 else 'TT')