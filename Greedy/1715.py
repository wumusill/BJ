import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    heapq.heappush(heap, num)

ans = 0

# 가장 작은 카드 뭉치 두 개를 빼서 합침
# 합친 카드 뭉치를 다시 힙에 삽입
# 두 개를 하나로 계속 합치므로 n - 1번 시행
if n == 1:
    print(ans)
else:
    for i in range(n - 1):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)

        res = a + b
        ans += res
        heapq.heappush(heap, res)

    print(ans)


# 4
# 20
# 30
# 30
# 40
# 240


# 4
# 1
# 3
# 2
# 4
# 19