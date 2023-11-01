# 시간 초과
import sys

n = int(sys.stdin.readline())
ramen = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

deadline = [0] * (n + 1)
ramen.sort(key=lambda x: -x[1])

for d, r in ramen:
    if deadline[d] == 0:
        deadline[d] = r
    else:
        for i in range(d, 0, -1):
            if deadline[i] == 0:
                deadline[i] = r
                break

print(sum(deadline))
#############################################################################
import sys
import heapq

n = int(sys.stdin.readline())
ramen = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 0번 index 기준 오름차순 정렬
# 0번 index 값이 동일하다면 1번 index 기준 오름차순
ramen.sort()

q = []

# 작은 deadline부터 순회
# 라면 개수를 힙에 삽입
for d, r in ramen:
    heapq.heappush(q, r)
    # 만약 라면의 개수가 deadline보다 크다면 가장 작은 라면 개수 제거
    if d < len(q):
        heapq.heappop(q)

print(sum(q))