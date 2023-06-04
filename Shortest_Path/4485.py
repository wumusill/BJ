import heapq
import sys

t = 0
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    # t 번째 테케
    t += 1
    h = []
    mat = []
    cost = [[int(1e9) for _ in range(n)] for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # matrix 설정
    for _ in range(n):
        mat.append(list(map(int, sys.stdin.readline().strip().split())))

    # (비용, x, y)
    heapq.heappush(h, (mat[0][0], 0, 0))

    # 비용
    cost[0][0] = mat[0][0]
    while h:
        c, x, y = heapq.heappop(h)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if cost[nx][ny] > cost[x][y] + mat[nx][ny]:
                nc = cost[x][y] + mat[nx][ny]
                cost[nx][ny] = nc
                heapq.heappush(h, (nc, nx, ny))

    print(f'Problem {t}: {cost[-1][-1]}')