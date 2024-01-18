import sys


def solution(player, res):
    global answer
    if player == 11:                                        # 선수가 11명 채워지면
        answer = max(answer, res)                           # 능력치 최댓값 갱신
        return                                              # 재귀 종료

    for i in range(11):                                     # 현재 선수 포지션 11개 순회
        if not visited[i] or not players[player][i]:        # 이미 선수가 있거나, 포지션에 뛸 수 없으면 패스
            continue
        visited[i] = False                                  # 포지션에 선수 할당
        solution(player + 1, res + players[player][i])      # 다음 선수 모든 포지션에 대해 재귀 수행
        visited[i] = True                                   # 선수 할당 취소


n = int(sys.stdin.readline())

for _ in range(n):
    players = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]

    # 포지션 할당 가능한지 아닌지
    visited = [True] * 11
    answer = 0
    solution(0, 0)
    print(answer)

# 1
# 10 0 0 0 0 0 0 0 0 0 0
# 0 10 0 0 0 0 0 0 0 0 0
# 0 0 10 1 0 0 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0 0 0 0
# 0 0 0 0 0 0 1 0 0 0 0
# 0 0 0 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0 0 0 0 1
# 29