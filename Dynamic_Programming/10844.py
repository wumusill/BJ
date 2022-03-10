n = int(input())

answer_dp = [1] * 10
if n == 1:
    print(sum(answer_dp[1:]))
else:
    for _ in range(2, (n + 1)):
        temp_dp = [0] * 10
        for i in range(1, 9):
            temp_dp[0] = answer_dp[1]
            temp_dp[i] = answer_dp[i-1] + answer_dp[i+1]
            temp_dp[9] = answer_dp[8]
        answer_dp = temp_dp

    print((sum(answer_dp) - answer_dp[0]) % 1000000000)