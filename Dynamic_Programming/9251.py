import sys

a = ' ' + sys.stdin.readline().rstrip()
b = ' ' + sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(b))] for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])

# 예시 입력
# ACAYKP
# CAPCAK

# 연산 전 dp
# [    ''  C  A  P  C  A  K'
#  ''  [0, 0, 0, 0, 0, 0, 0],
#   A  [0, 0, 0, 0, 0, 0, 0],
#   C  [0, 0, 0, 0, 0, 0, 0],
#   A  [0, 0, 0, 0, 0, 0, 0],
#   Y  [0, 0, 0, 0, 0, 0, 0],
#   K  [0, 0, 0, 0, 0, 0, 0],
#   P  [0, 0, 0, 0, 0, 0, 0],
# ]

# 연산 후 dp
# [    ''  C  A  P  C  A  K'
#  ''  [0, 0, 0, 0, 0, 0, 0],
#   A  [0, 0, 1, 1, 1, 1, 1],
#   C  [0, 1, 1, 1, 2, 2, 2],
#   A  [0, 1, 2, 2, 2, 3, 3],
#   Y  [0, 1, 2, 2, 2, 3, 3],
#   K  [0, 1, 2, 2, 2, 3, 4],
#   P  [0, 1, 2, 3, 3, 3, 4],
# ]

# 참고 : https://twinw.tistory.com/126