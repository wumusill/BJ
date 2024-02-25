import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
dp = [[l[i]] for i in range(n)]                         # 자기 자신을 원소로 갖는 dp로 초기화

for i in range(n):
    for j in range(i):
        if l[i] > l[j]:                                 # 현재 원소가 앞 원소보다 크다면
            temp = dp[j] + [l[i]]                       # temp : [앞 원소의 부분 수열 + 현재 원소]
            if len(dp[i]) < len(temp):                  # 지금 기록된 경우보다 temp가 더 크다면
                dp[i] = temp                            # temp 기록

answer = []
for res in dp:                                          # dp에서 길이가 가장 긴 list 정답으로 설정 후 출력
    if len(answer) < len(res):
        answer = res

print(len(answer))
print(*answer)