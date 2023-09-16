# 메모리 초과
import sys

n, s, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
dp = [[s]]

# 이전 곡 볼륨 순회
for i in range(n):
    pre_vol = dp[i]
    now_vol = []
    # 이전 볼륨에서 가능한 볼륨 계산
    for vol in pre_vol:
        vol1 = vol - l[i]
        vol2 = vol + l[i]
        if vol1 >= 0:
            now_vol.append(vol1)
        if vol2 <= m:
            now_vol.append(vol2)
    # dp에 현재 곡 가능한 볼륨 추가
    if now_vol:
        dp.append(now_vol)
    # 만약 현재 곡에 가능한 볼륨이 없다면 -> 마지막 곡까지 완주가 불가능하다면 -1 출력
    else:
        print(-1)
        break
# for문을 끝까지 순회했다면 -> 마지막 곡까지 완주했다면
# 마지막 곡의 최대 볼륨 출력
else:
    print(max(dp[-1]))
####################################################################################
# dp를 큐로 해도 메모리 초과
import sys
from collections import deque

n, s, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
dp = deque([[s]])

# 이전 곡 볼륨 순회
for i in range(n):
    pre_vol = dp.popleft()
    now_vol = []
    # 이전 볼륨에서 가능한 볼륨 계산
    for vol in pre_vol:
        vol1 = vol - l[i]
        vol2 = vol + l[i]
        if vol1 >= 0:
            now_vol.append(vol1)
        if vol2 <= m:
            now_vol.append(vol2)
    # dp에 현재 곡 가능한 볼륨 추가
    if now_vol:
        dp.append(now_vol)
    # 만약 현재 곡에 가능한 볼륨이 없다면 -> 마지막 곡까지 완주가 불가능하다면 -1 출력
    else:
        print(-1)
        break
# for문을 끝까지 순회했다면 -> 마지막 곡까지 완주했다면
# 마지막 곡의 최대 볼륨 출력
else:
    print(max(dp[-1]))
####################################################################################
import sys

n, s, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

# row : 곡의 개수,  col: 연주 가능한 볼륨
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 첫 곡의 볼륨(idx)
dp[0][s] = 1

# 그 다음 곡부터 순회
for i in range(n):
    for j in range(m + 1):
        # i번 째 곡의 볼륨 j
        if dp[i][j] == 1:
            # 연주 가능한 볼륨 계산
            vol1 = j + l[i]
            vol2 = j - l[i]
            # 연주 가능 볼륨이면 dp 갱신
            if vol1 <= m:
                dp[i + 1][vol1] = 1
            if vol2 >= 0:
                dp[i + 1][vol2] = 1

ans = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        ans = i
        break

print(ans)