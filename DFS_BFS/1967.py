# 트리 지름 구하기
# 1. 트리에서 아무 노드나 잡고 그 노드에서 가장 먼 노드(n1)를 구한다.
# 2. n1에서 가장 먼 노드(n2)를 구한다.
# 3. n1과 n2의 거리가 트리의 지름이다.
import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]

# 양방향 그래프로 저장 : 자식 노드에서도 부모 노드로 접근이 가능해야 함
for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append((b, c))
    tree[b].append((a, c))


# 가장 먼 거리 구하는 함수
def dfs(n, node):
    visited = [True] * (n + 1)
    visited[node] = False
    far_node, distance = 0, 0
    stack = []
    for b, c in tree[node]:                         # 출발 노드와 인접한 노드 순회
        stack.append((b, c))                        # 인접한 노드와 거리 스택 삽입
        visited[b] = False                          # 인접한 노드 방문 처리

    while stack:
        now, dist = stack.pop()
        if dist > distance:                         # 현재 노드의 거리가 더 출발노드로부터 더 멀다면
            distance = dist                         # 최장거리 갱신
            far_node = now                          # 가장 먼 노드 갱신

        for b, c in tree[now]:                      # 현재 노드와 인접한 노드와 거리 순회
            if visited[b]:                          # 인접 노드에 방문한 적 없다면
                stack.append((b, c + dist))         # 스택에 인접 노드와 출발 노드로부터의 거리 삽입
                visited[b] = False                  # 방문 처리

    return far_node, distance                       # 가장 먼 노드와 거리 반환


node1, dist1 = dfs(n, 1)                      # 특정 노드(root)에서 가장 먼 노드(node1)와 거리(dist1) 계산
node2, answer = dfs(n, node1)                       # node1과 가장 먼 노드(node2)와 answer(=node1, node2의 거리) 계산

print(answer)