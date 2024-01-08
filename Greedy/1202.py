# 가방에 최대 가치의 보석을 담되 용량이 작은 가방부터 보석을 담는다
# 3% 에서 틀리는데 모르겠다 보류
import sys

n, k = map(int, sys.stdin.readline().split())

jewels = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    jewels.append((m, v))
jewels.sort(key=lambda x: (x[1], x[0]))

bags = []
for _ in range(k):
    bag = int(sys.stdin.readline())
    bags.append(bag)
bags.sort(reverse=True)

ans = 0
while bags:
    bag = bags.pop()
    while jewels:
        w, v = jewels.pop()
        if w <= bag:
            ans += v
            break

print(ans)
###############################################################################
import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline().rstrip()) for _ in range(k)]

jewels.sort()
bags.sort()

heap = []
answer = 0
for bag in bags:                              # 작은 가방부터 순회
    while jewels and jewels[0][0] <= bag:     # 작은 무게의 보석부터 순회
        heapq.heappush(heap, -jewels[0][1])   # 담을 수 있는 보석이면 전부 heap에 추가, 최소힙에서 최고 가치가 앞에 오도록 음수로 저장
        heapq.heappop(jewels)                 # 보석 맨 앞에 것 pop
    if heap:
        answer -= heapq.heappop(heap)         # 담을 수 있는 보석(heap) 중 최고 가치 보석 하나 가방에 담음

print(answer)