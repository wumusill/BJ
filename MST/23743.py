import sys


def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def union(parent, a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, sys.stdin.readline().split())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# 비상 탈출구를 0번 노드로 설정한 뒤, 비용을 line에 추가 (0, node, exit_cost)
exits = list(map(int, sys.stdin.readline().split()))
for i in range(1, n + 1):
    lines.append([0, i, exits[i - 1]])

# 비용 기준 오름차순 정렬
lines.sort(key=lambda x: x[2])
parent = [i for i in range(n + 1)]
answer = 0

# 크루스칼 알고리즘 수행
for a, b, c in lines:
    a, b = find(parent, a), find(parent, b)
    if a != b:
        union(parent, a, b)
        answer += c

# print(parent)
print(answer)