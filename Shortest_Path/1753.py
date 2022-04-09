import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for i in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

'''
입력 예시
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

노드 4에 대한 처리에서 4번 노드까지의 최단거리 (1) + 4번에서 3번 노드로 가는 거리 
(3) 이라면 우선순위 큐에 (거리:4, 노드:3) 담김
그런데 노드 5에 대한 처리에서 5번 노드까지의 최단거리 (2) + 5번에서 3번 노드로 가는 거리 
(2)인 3 이라면, 기존의 4보다 작다. 
따라서 우선순위 큐에 (거리:3, 노드:3)이 담긴다.

if distance[now] < dist:
    continue
    
위 코드가 실행된다면
우선순위로 꺼낸 원소에는 3번(now)까지 최단 거리 4(dist)라는 정보가 들어있다.
하지만 현재 최단 거리 테이블에서 3번 노드까지 최단 거리(distance[now])는 3이다.
따라서 현재 노드인 3번(now)에 대해서는 무시(continue)하면 된다.
```