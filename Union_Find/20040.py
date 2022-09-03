import sys

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = parent[y]
    else:
        parent[y] = parent[x]


for answer in range(1, m + 1):
    a, b = map(int, sys.stdin.readline().split())
    # 부모가 같은 것을 연결하면 사이클이 생김
    if find(a) == find(b):
        print(answer)
        break
    union(a, b)

# 끝까지 for문이 돌면 실행
else:
    print(0)