import sys

n = int(sys.stdin.readline())
if n < 3:
    print(1)
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    # 첫 자릿수는 0이 될 수 없으므로 무조건 1
    # 연속으로 1이 못오므로 1단계 아래 경우의 수들은 올 수 없음 -> 2단계 아래 모든 경우의 수와 결합 가능
    # +1 은 뒤가 모두 0인 경우 
    for i in range(3, n + 1):
        dp[i] = sum(dp[:i - 1]) + 1

    print(dp[n])