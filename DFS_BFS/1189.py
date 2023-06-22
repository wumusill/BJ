import sys

n, m, k = map(int, sys.stdin.readline().strip().split())
mat = [list(sys.stdin.readline().strip()) for _ in range(n)]
ans = 0


def dfs(x, y, res):
    global ans
    if x == 0 and y == m - 1 and res == k:
        ans += 1
        return
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # visited를 활용한 방문 표시는 최단 경로는 구할 수 있지만 모든 경우의 수를 구할 수 없음
        if mat[nx][ny] == '.':
            # 일단 방문 표시 대신 벽으로 막아서 다시 돌아오지 못하게 함
            mat[nx][ny] = 'T'
            dfs(nx, ny, res + 1)
            # 모든 경우의 수 탐색 후 다른 경우의 수를 위해 벽으로 막은 곳 원상 복구
            mat[nx][ny] = '.'


mat[n - 1][0] = 'T'
dfs(n - 1, 0, 1)
print(ans)