# 부모가 같다면 여행 가능
# 마지막 줄에 주어진 도시들이 모두 다 같은 부모를 가지고 있는지 판단
import sys


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [i for i in range(n)]
graph = []

for _ in range(n):
    connect = list(map(int, sys.stdin.readline().rstrip().split()))
    graph.append(connect)

for i in range(n):
    for j in range(i, n):
        if graph[i][j] == 1:
            union(parent, i, j)

plan = list(map(int, sys.stdin.readline().rstrip().split()))

# index를 맞춰주기 위해 -= 1
for i in range(len(plan)):
    plan[i] -= 1

res = []
# union을 해도 부모가 다를 수 있다. root 부모를 찾아 추가
for city in plan:
    root_parent = find(parent, city)
    res.append(root_parent)

# 부모 값이 한 개면 YES
if len(set(res)) != 1:
    print("NO")
else:
    print("YES")


# 4
# 4
# 0 0 0 1
# 0 0 1 0
# 0 1 0 1
# 1 0 1 0
# 3 1 2 4
# YES