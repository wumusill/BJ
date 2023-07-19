import sys
import heapq

n = int(sys.stdin.readline())

# 초기화
mat = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
cost = [[int(1e9) for _ in range(n)] for _ in range(n)]
heap = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 출발지 설정
cost[0][0] = 0
heapq.heappush(heap, (0, 0, 0))

# 비용은 색 교체 수
while heap:
    c, x, y = heapq.heappop(heap)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if c < cost[nx][ny]:
            # 흰 방이면 그냥 통과
            if mat[nx][ny] == 1:
                cost[nx][ny] = c
                heapq.heappush(heap, (c, nx, ny))
            # 검은 방이면 흰 방으로 색 교체
            else:
                cost[nx][ny] = c + 1
                heapq.heappush(heap, (c + 1, nx, ny))

print(cost[-1][-1])