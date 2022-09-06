# 문제에 정의된 비용 계산 방법 = min(|xA-xB|, |yA-yB|, |zA-zB|)
# 따라서 x, y, z를 기준으로 각각 정렬하고 앞뒤 노드 연결 비용 계산
# 계산된 비용을 모두 list에 넣고 오름차순 정렬 가장 저렴한 n-1개로 연결
import sys


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(sys.stdin.readline())
planets = []
parent = [_ for _ in range(n)]

for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    planets.append((i, x, y, z))

x_sort = sorted(planets, key=lambda x: x[1])
y_sort = sorted(planets, key=lambda x: x[2])
z_sort = sorted(planets, key=lambda x: x[3])

edgs = []
# a 행성에서 a+1 행성으로 x 축으로 이동하는 간선, 비용
for a in range(n - 1):
    edge = (abs(x_sort[a + 1][1] - x_sort[a][1]), x_sort[a][0], x_sort[a + 1][0])
    edgs.append(edge)

# a 행성에서 a+1 행성으로 y 축으로 이동하는 간선, 비용
for a in range(n - 1):
    edge = (abs(y_sort[a + 1][2] - y_sort[a][2]), y_sort[a][0], y_sort[a + 1][0])
    edgs.append(edge)

# a 행성에서 a+1 행성으로 z 축으로 이동하는 간선, 비용
for a in range(n - 1):
    edge = (abs(z_sort[a + 1][3] - z_sort[a][3]), z_sort[a][0], z_sort[a + 1][0])
    edgs.append(edge)

# 간선들 거리순 정렬
edgs.sort(key=lambda x: x[0])

answer = 0
for cost, a, b in edgs:
    if find(a) != find(b):
        union(a, b)
        answer += cost

print(answer)

# 4
# 6
# 0 0 0
# 1 1 1
# -5 -5 -5
# -6 -6 170
# -1 -1 170
# -4 -4 172