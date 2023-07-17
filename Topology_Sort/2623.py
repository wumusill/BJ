import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
q = deque()
res = []

for _ in range(m):
    l = list(map(int, sys.stdin.readline().split()))
    pd = l[0]
    for i in range(1, pd):
        graph[l[i]].append(l[i + 1])
        indegree[l[i + 1]] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    res.append(x)
    for i in graph[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

# 조건 : 순서를 정하는 것이 불가능한 경우 0 출력
if len(res) != n:
    print(0)
else:
    for ans in res:
        print(ans)