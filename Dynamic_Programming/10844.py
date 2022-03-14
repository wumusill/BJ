# 자릿수, 맨 앞자리 인덱스별 뒷자리 개수, 총 합계, 정답 (맨 앞 0 제외)
# 1, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 10, 9
# 2, [1, 2, 2, 2, 2, 2, 2, 2, 2, 1] 18, 17
# 3, [2, 3, 4, 4, 4, 4, 4, 4, 3, 2] 34, 32
# 4, [3, 6, 7, 8, 8, 8, 8, 7, 6, 3] 64, 61

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
# 3
# 32

# 4
# 61

# 5
# 116