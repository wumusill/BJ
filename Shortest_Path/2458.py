# 본인보다 키가 작거나 큰 인원이 (n - 1)명이라면 자신의 키 순서를 알 수 있음
import sys

n, m = map(int, sys.stdin.readline().split())
height = [[False for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    height[a][b] = True                                 # height[a][b] = True : a는 b보다 키가 작음

for k in range(1, n + 1):                               # 플로이드 워셜 알고리즘 수행
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if height[a][k] and height[k][b]:           # a가 k보다 작고, k가 b보다 작다면 a는 b보다 작음
                height[a][b] = True

answer = 0
for a in range(1, n + 1):
    know = 0
    for b in range(1, n + 1):
        know += height[a][b] + height[b][a]             # 본인보다 키가 작거나 키가 큰 인원 합계 계산
    if know == n - 1:                                   # 합계가 본인을 제외한 n - 1 이라면, 키 순서를 알 수 있음
        answer += 1                                     # 키 순서 알 수 있는 인원 갱신

print(answer)