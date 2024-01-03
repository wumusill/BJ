import sys

n, m = map(int, sys.stdin.readline().split())
l = list(sys.stdin.readline().split())
gender = {i + 1 : l[i] for i in range(n)}

graph = [[] for _ in range(n + 1)]
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
lines.sort(key=lambda x: x[2])


def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


parent = [i for i in range(n + 1)]
answer = 0
for a, b, c in lines:
    # 부모 노드뿐만 아니라 여초 남초가 달라야 연결 가능
    if find(parent, a) != find(parent, b) and gender[a] != gender[b]:
        union(parent, a, b)
        answer += c

# 모든 노드의 부모가 같은지 확인
# 부모가 다르면, 모든 학교를 연결할 수 있는 경로가 없다는 것
res = find(parent, 1)
for i in range(2, n + 1):
    next = find(parent, i)
    if res != next:
        print(-1)
        break
    res = next
else:
    print(answer)