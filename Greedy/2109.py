import sys
import heapq

n = int(sys.stdin.readline())

# [pay, deadline]
lectures = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# deadline을 기준으로 오름차순 정렬
lectures.sort(key=lambda x: x[1])

h = []
for pay, deadline in lectures:      # 강의 정보 순회
    heapq.heappush(h, pay)          # 가격을 힙에 삽입
    if len(h) > deadline:           # 만약 힙의 길이가 현재 데드라인을 초과한다면
        heapq.heappop(h)            # 가장 가격이 낮은 강의 힙에서 제거

print(sum(h))

# 5
# 3 3
# 2 3
# 1 3
# 100 4
# 90 4
# 195