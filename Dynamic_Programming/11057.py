import sys

n = int(sys.stdin.readline())
dp = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

for i in range(2, n + 1):
    case = [0] * 10
    for j in range(10):
        case[j] = sum(dp[-1][j:])
    dp.append(case)

print(sum(dp[-1]) % 10007)

# n = 1일 때
    # 0 ~ 9 : 10개
# n = 2일 때
    # 0뒤에 올 수 있는 수 0 ~ 9 : 10개
    # 1뒤에 올 수 있는 수 1 ~ 9 : 9개
    # 2뒤에 올 수 있는 수 2 ~ 9 : 8개
    # 9뒤에 올 수 있는 수 8 ~ 9 : 2개
# n = 3일 때
    # 0뒤에 올 수 있는 수는 2째 자리가 0 ~ 9인 수들
    # 5뒤에 올 수 있는 수는 2째 자리가 5 ~ 9인 수들
    # 8뒤에 올 수 있는 수는 2째 자리가 8 ~ 9인 수들