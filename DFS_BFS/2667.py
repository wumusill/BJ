n = int(input())
graph = []

cnt = 0
l_num_apt = []
num_apt = 0

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        global num_apt
        num_apt += 1

        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            l_num_apt.append(num_apt)
            num_apt = 0

print(len(l_num_apt))
for i in sorted(l_num_apt):
    print(i)


# 다른 사람의 BFS를 이용한 풀이