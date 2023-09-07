# 시작 시간을 기준으로 오름차순 정렬
# 강의 시간 하나씩 순회
# 종료 시간을 힙에 삽입 -> 힙의 첫 원소는 항상 가장 빨리 끝나는 강의 종료 시간
# 탐색 중인 강의 시작 시간이 힙의 최솟값보다 크거나 같으면 -> 해당 강의실에 강의 배정
# 탐색 중인 강의 시작 시간이 힙의 최솟값보다 작다면 -> 새로운 강의실 오픈
import sys
import heapq

n = int(sys.stdin.readline())
l = []
heap = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    l.append((start, end))

l.sort()

heapq.heappush(heap, l[0][1])
ans = 1

for i in range(1, n):
    start, end = l[i][0], l[i][1]
    if start >= heap[0]:
        heapq.heappop(heap)
    else:
        ans += 1
    heapq.heappush(heap, end)

print(ans)