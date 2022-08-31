import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
answer = 0

# 구간 합 기록하는 list
sum_l = [0] * n
sum_l[0] = l[0]

# 구간별 m으로 나눈 나머지 개수를 기록하기 위한 list, 나머지는 무조건 m 이하
# 나머지가 같은 구간 끼리 고르면 그 구간 합은 m으로 나누어 떨어진다
mod_l = [0] * m

res = 0
# 구간 합 list에 기록하는 반복문
for i in range(n):
    res += l[i]
    # 나머지에 해당하는 index에 += 1
    mod_l[res % m] += 1
    # res 가 나누어 떨어지면 == 원소 자체가 약수이면, answer += 1
    if res % m == 0:
        answer += 1
    sum_l[i] = res

for j in mod_l:
    # 나머지의 개수가 0이면 패스
    if j == 0:
        continue
    # 나머지가 1개 이상이면 거기서 구간을 선택할 수 있는 경우의 수, 4C2를 answer 에 더한다
    cnt = j * (j - 1) // 2
    answer += cnt

print(answer)