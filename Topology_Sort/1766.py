# q 대신 힙을 사용해서 pop(=popleft)시 항상 가장 쉬운 문제(최솟값)가 나올 수 있도록 하기
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
heap = []
ans = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    x = heapq.heappop(heap)
    ans.append(x)
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)

print(*ans)