import sys

n = sys.stdin.readline().strip()


# 자릿수의 개수
# 한 자릿수 숫자는 9개, 두 자릿수 숫자는 90개...
# dp = [9, 90, 900, 9000, 90000, 900000, 900000, 90000000]

# 각 자릿수의 개수만큼 곱하면
# dp = [9, 180, 2700, 36000, 450000, 5400000, 6300000, 720000000]

# 구하는 자릿수 하나 아래 자릿수의 합계 계산
# 240 이라면 두 자릿수까지의 숫자 개수 합계 계산
ans = 0
for i in range(len(n) - 1):
    ans += 9 * (10 ** i) * (i + 1)

# 한 자릿수는 그대로 출력
if len(n) == 1:
    ans = int(n)

# 두 자릿수 이상부터
else:
    # 구하는 자릿수 숫자의 개수 계산
    # 240 이라면 3자릿수는 141개, 숫자의 개수는 * 3
    ans += ((int(n) - 10 ** (len(n) - 1)) + 1) * len(n)

print(ans)