import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    _min = int(1e9)
    j = 1
    while (j ** 2) <= i:
        _min = min(_min, dp[i - (j ** 2)])
        j += 1
    dp[i] = _min + 1

print(dp[n])

# n보다 작거나 같은 제곱수를 찾고 (n - 제곱수)를 인덱스로 가진 값에 1을 더해주면 된다.
# = dp[i - (j ** 2)] + 1
# 시간초과, pypy3만 통과
###############################################################################

'''
주어진 값 n이 제곱수이면 1 
(n - i ** 2)를 하고 남은 수가 제곱수면 2
(n - i ** 2 - j ** 2)를 하고 남은 수가 제곱수면 3
나머지는 4
'''

n = int(sys.stdin.readline())


def solution(n):
    sqrt = n ** 0.5
    if int(sqrt) == sqrt:
        return 1
    for i in range(1, int(sqrt) + 1):
        if int((n - i ** 2) ** 0.5) == (n - i ** 2) ** 0.5:
            return 2
    for i in range(1, int(sqrt) + 1):
        for j in range(1, int((n - i ** 2) ** 0.5) + 1):
            if int((n - i ** 2 - j ** 2) ** 0.5) == (n - i ** 2 - j ** 2) ** 0.5:
                return 3
    return 4


print(solution(n))