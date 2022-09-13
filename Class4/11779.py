import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
# visited[2][0]은 2번 노드로 가는 최소 거리 기록
# visited[2][1]은 2번 노드 방문 전 노드 번호 기록
visited = [[INF] * 2 for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


def solution(start, end):
    q = []
    visited[start][0] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > visited[now][0]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 노드로 가기 위한 비용과 그 전 노드 번호를 기록
            if visited[i[0]][0] > cost:
                visited[i[0]][0] = cost
                visited[i[0]][1] = now
                heapq.heappush(q, (cost, i[0]))
    return visited[end]


start, end = map(int, sys.stdin.readline().split())

print(solution(start, end)[0])

# 도착 노드에서부터 역으로 어디서 왔는지 추적
course = []
node = end
while True:
    # 출발 노드에 다다르면 break
    if node == start:
        break
    course.append(node)
    node = visited[node][1]
course.append(start)

print(len(course))
for _ in range(len(course)):
    answer = course.pop()
    print(answer, end=' ')