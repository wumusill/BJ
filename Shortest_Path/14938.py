import sys
import heapq


def solution(start):
    h = []
    heapq.heappush(h, (0, start))                               # 출발 노드 설정
    dp[start] = 0

    while h:
        cost, now = heapq.heappop(h)
        if dp[now] < cost:                                      # 이미 더 짧은 최단 거리가 있다면 continue
            continue

        for next, c in graph[now]:
            new_cost = cost + c
            if new_cost < dp[next]:                             # 기록된 최단 거리보다 짧다면 힙에 삽입하여 다음 노드 탐색
                heapq.heappush(h, (new_cost, next))
                dp[next] = new_cost


n, m, r = map(int, sys.stdin.readline().split())
item = [0] + list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])                                     # 양방향 그래프
    graph[b].append([a, c])

answer = 0
for start in range(1, n + 1):
    dp = [int(1e9)] * (n + 1)                                   # 출발 노드부터 index 노드까지의 최단 거리 기록
    solution(start)

    result = 0
    for i in range(1, n + 1):
        if dp[i] <= m:                                          # index 노드까지의 최단 거리가 m 이하라면 index 노드의 item 수집
            result += item[i]

    answer = max(answer, result)                                # 수집 가능한 item 최댓값 갱신

print(answer)