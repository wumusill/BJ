# 트리의 지름 구하기
# 1. 특정 노드로부터 가장 먼 노드(n1)의 거리를 구한다.
# 2. n1로부터 가장 먼 노드(n2)의 거리를 구한다.
# 3. 2번에 구한 거리가 트리의 지름
import sys

# 노드의 개수
v = int(sys.stdin.readline())

# 간선 정보 받아 저장
tree = [[] for _ in range(v + 1)]
for _ in range(v):
    l = list(map(int, sys.stdin.readline().split()))
    node = l[0]
    for i in range(1, len(l) - 1, 2):
        tree[node].append((l[i], l[i + 1]))


# 파라미터 노드로부터 가장 먼 노드와 거리 반환
def dfs(node):
    far_node, distance = 0, 0

    visited = [True] * (v + 1)
    visited[node] = False
    stack = []

    for b, c in tree[node]:
        stack.append((b, c))
        visited[b] = False

    while stack:
        now, dist = stack.pop()
        if dist > distance:
            distance = dist
            far_node = now
        for b, c in tree[now]:
            if visited[b]:
                stack.append((b, dist + c))
                visited[b] = False

    return far_node, distance


# 특정 노드(1번)로부터 가장 먼 노드와 거리
node1, dist1 = dfs(1)

# node1과 가장 먼 노드와 거리(=트리의 지름)
node2, answer = dfs(node1)
print(answer)