import sys
from collections import deque

n = int(sys.stdin.readline())

# 그래프와 진입 차수 기록
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]

# 비용과 정답 기록
cost = [0 for _ in range(n + 1)]
ans = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    input_l = list(map(int, sys.stdin.readline().split()))
    cost[i] = input_l[0]                    # 비용 기록
    needed_building = input_l[1:-1]
    for j in needed_building:
        graph[j].append(i)                  # 그래프 기록
        indegree[i] += 1

# 진입 차수가 0인 건물(아무 사전 조건 없이 지을 수 있는 건물) 번호 큐에 삽입
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    # ans[건물 번호] += 현재 짓는 건물의 비용
    x = q.popleft()
    ans[x] += cost[x]

    # 그 다음 지을 수 있는 건물 번호 순회
    # 사전 조건 건물 개수 -= 1
    # ans[다음 건물 번호] 갱신
    # 다음 건물을 짓기 위해 필요한 비용이 저장 됨
    for i in graph[x]:
        indegree[i] -= 1
        ans[i] = max(ans[i], ans[x])

        if indegree[i] == 0:
            q.append(i)

for i in range(1, n + 1):
    print(ans[i])