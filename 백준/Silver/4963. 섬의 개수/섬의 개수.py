import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    global m, v
    if x < 0 or y < 0 or x >= h or y >= w:  # 좌표가 맵의 범위를 벗어나면 종료
        return False

    if v[x][y] and m[x][y] == 1:            # 방문 가능한 섬이면
        v[x][y] = False                     # 방문 처리 후 dfs 수행
        dfs(x + 1, y)                       # 상하좌우 dfs
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

        dfs(x + 1, y + 1)                   # 대각선 dfs
        dfs(x + 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x - 1, y - 1)


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    answer = 0
    m = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    v = [[True for _ in range(w)] for _ in range(h)]

    for i in range(h):                          # 지도 순회
        for j in range(w):
            if v[i][j] and m[i][j] == 1:        # 방문 가능한 육지를 만나면
                answer += 1                     # 섬 개수 갱신 후 dfs 수행
                dfs(i, j)

    print(answer)