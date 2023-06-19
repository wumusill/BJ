import sys

n = int(sys.stdin.readline().strip())

# n까지만 확인하면 된다
# (n+1)번 째와 n번 째의 차이가 n보다 크기 때문
l = [True] * (n + 1)
sosu = []

# 0부터 n까지 소수인 숫자 찾기
for i in range(n + 1):
    if i < 2:
        l[i] = False
        continue
    elif l[i] == True:
        sosu.append(i)
        for j in range(i * 2, n + 1, i):
            l[j] = False

# 찾은 소수들로 누적합 리스트 계산
res = 0
cumulative_sosu = [0]
for num in sosu:
    res += num
    cumulative_sosu.append(res)

# 투포인터 계산
left, right = 0, 1
ans = 0

while right < len(cumulative_sosu):
    if cumulative_sosu[right] - cumulative_sosu[left] < n:
        right += 1
    elif cumulative_sosu[right] - cumulative_sosu[left] == n:
        ans += 1
        left += 1
    else:
        left += 1

print(ans)