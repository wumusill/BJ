import sys

n, m = map(int, sys.stdin.readline().strip().split())

# 누적합 리스트에서 특정 구간부터가 아닌 처음부터의 합계를 계산하기 위해 맨 앞에 0을 추가
nums = [0] + list(map(int, sys.stdin.readline().strip().split()))
res = 0
stack_list = []

# 누적합 계산
for num in nums:
    res += num
    stack_list.append(res)

# 투포인터
a, b = 0, 1
ans = 0

# b가 끝까지 탐색할 때까지 반복
while b < n + 1:
    # 연속합 계산
    res = stack_list[b] - stack_list[a]

    # 연속합이 타겟과 같다면 경우의 수 추가, b를 뒤로 한 칸 이동, a를 뒤로 한 칸 이동해도 상관 없음
    if res == m:
        ans += 1
        b += 1
    # 연속합이 타겟보다 크면 a를 뒤로 한 칸 이동
    elif res > m:
        a += 1
    # 연속합이 타겟보다 작으면 b를 뒤로 한 칸 이동
    else:
        b += 1

print(ans)