import sys


def solution():
    global answer
    for i in range(2, int(MAX ** 0.5) + 1):
        # 제곱 수로 나누어 떨어지는 수 중 MIN 보다 크거나 같으면서 가장 가까운 수(a) 구하기
        # a = (((MIN - 1) // square) + 1) * square
            # 제곱 수로 나누어 떨어진다면 자기 자신이 나와야 함
            # 제곱 수로 나누어 떨어지지 않는다면 자기보다 크면서 제곱 수로 나누어 떨어지는 수 중 가장 작은 수가 나와야 함
            # 예시 범위 : [4, 5, 6, 7, 8, 9]
            # 예시 결과 : [4, 9, 9, 9, ., 9] -> 8은 4로 나누어 떨어지기 때문에 계산하지 않음

        square = i ** 2                  # 제곱 수
        a = MIN - 1                      # 제곱 수로 나누어 떨어지는 수(9)까지는 이전과 같은 수가 나와야 하므로 (-1)
        a //= square                     # 제곱 수가 안에 몇 개 들어가는지 파악
        a += 1                           # 몫보다 1 큰 수
        a *= square                      # 그 수에 제곱 수를 곱하면 MIN보다 크거나 같은 수 중 제곱 수로 나눠 떨어지는 가장 작은 수가 됨

        for j in range(a, MAX + 1, square): # MAX까지 순회하면서
            if answer[j - MIN]:             # 제곱 수로 나누어 떨어지는 수의 index False로 갱신
                answer[j - MIN] = False


MIN, MAX = map(int, sys.stdin.readline().split())
answer = [True] * (MAX - MIN + 1)           # 최댓값이 너무 커서 주어진 수의 범위만큼만 리스트 생성
solution()

print(sum(answer))