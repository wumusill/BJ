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

############################################################################
✅ BFS 
BFS = “큐 기반, 가까운 곳부터 차례대로 탐색”

1️⃣ 큐에서 하나를 꺼낸다
    → 현재 탐색할 좌표
2️⃣ 현재 좌표의 사방위(또는 8방위)를 확인한다
3️⃣ 각 방향 좌표가 유효한지 검사한다, 맵 범위 안인가?
4️⃣ 유효하다면 방문 가능한지 검사한다
    아직 방문하지 않았는가?
    조건(길/섬 등)을 만족하는가?
5️⃣ 방문 가능하면
    방문 처리한다
    큐에 넣는다
🔁 큐가 빌 때까지 반복
############################################################################
✅ DFS
DFS = “지금 위치에서 갈 수 있는 곳을 끝까지 탐색”

dfs(x, y)가 호출되었을 때

1️⃣ 현재 좌표(x, y)가 유효한지 검사한다
    맵 범위 안인가?
2️⃣ 방문 가능한 좌표인지 검사한다
    아직 방문하지 않았는가?
    조건(길/섬 등)을 만족하는가?
3️⃣ 방문 가능하다면
    방문 처리한다
4️⃣ 현재 좌표와 연결된 모든 방향으로 재귀 호출한다
    상 / 하 / 좌 / 우 (또는 8방위)
    👉 각 재귀 호출은
    같은 1️⃣~4️⃣ 과정을 반복
