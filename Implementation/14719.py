import sys

h, w = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
dp = [0] * w

for i in range(1, w - 1):                       # 블록 하나씩 순회
    left, right = max(l[:i]), max(l[i + 1:])    # 접근한 블록 기준 왼쪽, 오른쪽 각각 가장 높은 블록의 높이
    lower = min(left, right)                    # 가장 높은 왼쪽, 오른쪽 블록 중 더 낮은 블록
    dp[i] = lower - l[i]                        # 빗물은 현재 높이에서 lower의 높이까지 고임

ans = 0
for res in dp:
    if res > 0:                                 # 가장 높은 높이의 경우 dp[i] 음수가 나옴 = 빗물이 고이지 않음
        ans += res

print(ans)