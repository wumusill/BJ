# 시간 초과
import sys


def dfs(start, visited, team):
    global result

    next = pick[team[-1]]                           # 다음 지목된 학생
    if start == next:                               # 다음 지목된 학생이 첫 학생이라면
        result += len(team)                         # 팀원의 수 합산
        return

    if visited[next]:                               # 다음 지목된 학생 접근한적 없으면
        visited[next] = False                       # 접근 처리
        dfs(start, visited, team + [next])          # 재귀 수행
        visited[next] = True                        # 접근 처리 초기화


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    pick = [0] + list(map(int, sys.stdin.readline().split()))
    answer, result = len(pick), 0
    visited = [True] * (n + 1)

    for start in range(1, n + 1):
        visited[start] = False
        dfs(start, visited, [start])

    print(n - result)
####################################################################################
# 위 코드는 이미 접근했더라도 start 친구가 아니라면 계속 접근하게 됨
# 아래 코드는 한 번이라도 접근한 학생에게 다시는 접근하지 않음
import sys

sys.setrecursionlimit(10**6)                        # RecursionError 방지


def dfs(x):
    global result

    visited[x] = False                              # 현재 접근 학생
    cycle.append(x)                                 # 사이클에 추가
    next = pick[x]                                  # 다음 지목 학생

    if not visited[next]:                           # 만약 다음 지목 학생에게 접근한 적이 있다면
        if next in cycle:                           # 사이클에 포함되어 있는지 확인, 포함되어 있다면
            idx = cycle.index(next)                 # 그 학생의 index부터 사이클 발생
            result += len(cycle[idx:])              # 사이클의 길이 합산
    else:
        dfs(next)                                   # 접근한 적이 없다면 재귀 수행


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    pick = [0] + list(map(int, sys.stdin.readline().split()))
    answer, result = len(pick), 0
    visited = [True] * (n + 1)

    for x in range(1, n + 1):
        if visited[x]:
            cycle = []
            dfs(x)

    print(n - result)


# 2
# 3
# 2 3 3
# 4
# 2 3 4 2
# 2 1