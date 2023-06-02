# import sys
#
# n = int(sys.stdin.readline())
# l = list(map(int, sys.stdin.readline().split()))
#
# res = 0
# s = []
# for element in l:
#     res += element
#     s.append(res)
#
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         if s[j] - s[i] == 50:
#             ans += 1
#
# print(ans)
############################################################
# 틀린 이유
# 입력 값 순서대로 파이차트를 그리는 것이 아니라 입력들을 조합해서 최댓값을 구하는 것
import sys
from itertools import permutations


n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
ans = 0

# 입력 값들의 모든 순서 경우의 수
nPr = list(permutations(l))

# 경우의 수 하나씩 순회
for case in nPr:
    res = 0
    cnt = 0
    s = []
    # 경우의 수마다 누적합 리스트로 계산
    for element in case:
        res += element
        s.append(res)
    # 누적합 리스트에서 모든 원소들의 차이 계산
    # 차이가 50이면 원점을 지나는 직선이 있음
    for i in range(n - 1):
        for j in range(i + 1, n):
            if s[j] - s[i] == 50:
                cnt += 1

    # 직선의 개수 최댓값 갱신
    ans = max(ans, cnt)

print(ans)

# 테케
# 6
# 1 2 3 4 45 45
# 2
