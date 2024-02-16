# LCA : Lowest Common Ancestor, 최소 공통 조상
# 두 노드의 공통된 조상 중 가장 가짜운 공통 조상을 찾는 문제
# 알고리즘
# 1. 모든 노드에 대한 깊이를 계산
# 2. 최소 공통 조상을 찾을 두 노드를 확인
#     1. 먼저 두 노드의 깊이가 동일하도록 거슬러 올라감
#     2. 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라감
# 3. 모든 LCA(a, b) 연산에 대하여 2번 과정을 반복

# 먼저 DFS를 이용해 모든 노드에 대하여 깊이를 계산
# 매 쿼리마다 부모 방향으로 거슬러 올라가기 위해 최악의 경우 O(N)의 시간 복잡도
# 모든 쿼리를 처리할 때 시간 복잡도는 O(NM)
# Python3 시간 초과(93%), PyPy3로 제출하여 통과
import sys

sys.setrecursionlimit(int(1e5))


def dfs(x, depth):
    visited[x] = False           # 노드 방문 처리
    d[x] = depth                 # 깊이 기록
    for y in graph[x]:           # 다음 노드 순회
        if visited[y]:           # 방문한 적이 없는 노드라면, 방문할 수 있다면
            parent[y] = x        # 방문하지 않은 다음 노드의 부모는 현재 노드
            dfs(y, depth + 1)    # 자식 노드에 대하여 재귀 수행


def lca(a, b):
    while d[a] != d[b]:             # 두 노드의 깊이가 동일하도록 설정
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:                   # 두 노드의 조상이 같아질 때까지 반복
        a = parent[a]
        b = parent[b]

    return a                        # 같아진 조상 노드 반환


n = int(sys.stdin.readline())
parent = [0] * (n + 1)              # 부노 모드 기록
d = [0] * (n + 1)                   # 노드의 깊이 기록
visited = [True] * (n + 1)

# 그래프 정보 입력
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 노드의 부모와 깊이 연산
dfs(1, 0)

# LCA 수행
m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(lca(a, b))