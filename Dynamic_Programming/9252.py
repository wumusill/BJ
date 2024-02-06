import sys

a = ' ' + sys.stdin.readline().rstrip()
b = ' ' + sys.stdin.readline().rstrip()
dp = [['' for _ in range(len(b))] for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + a[i]
        else:
            x, y = dp[i - 1][j], dp[i][j - 1]
            dp[i][j] = x if len(x) > len(y) else y

answer = dp[-1][-1]
print(len(answer))
if len(answer):
    print(answer)