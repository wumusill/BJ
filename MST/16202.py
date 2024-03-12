import sys


def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution():
    global answer, lines
    parent = [i for i in range(n + 1)]
    result = 0

    for cost, a, b in lines:                                    # 크루스칼 알고리즘 수행
        a, b = find(parent, a), find(parent, b)
        if a != b:
            union(parent, a, b)
            result += cost

    p1 = find(parent, 1)                                        # MST가 되었는지 부모 노드 확인
    for i in range(2, n + 1):
        p2 = find(parent, i)
        if p1 != p2:                                            # MST가 아니면 비용 0
            answer.append(0)
            break
    else:                                                       # MST라면 비용 기록
        answer.append(result)

    lines = lines[1:]                                           # 가장 작은 비용의 간선 제거


n, m, k = map(int, sys.stdin.readline().split())
answer, lines = [], []

for i in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().split())
    lines.append([i, a, b])

for _ in range(k):
    solution()

print(*answer)