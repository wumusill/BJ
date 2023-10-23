# 양수는 정렬해서 큰 수는 무조건 묶는다
# 1은 무조건 더하기
# 음수도 정렬해서 절댓값이 큰 수는 무조건 묶는다
# 0은 상황따라 더하거나 음수와 묶음
import sys

n = int(sys.stdin.readline())
ans = 0

zero = 0
pos = []
neg = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        zero += 1
    elif num == 1:
        ans += 1
    elif num > 1:
        pos.append(num)
    elif num < 0:
        neg.append(num)

# 음수가 한 개인데 0이 있다면 묶음
if len(neg) == 1 and zero > 0:
    zero -= 1
    neg.pop()

# 절댓값 기준 오름차순 정렬
pos.sort()
neg.sort(reverse=True)

# 절댓값이 큰 순서대로 두 개씩 묶음
while len(pos) > 1:
    a = pos.pop()
    b = pos.pop()
    ans += a * b

while len(neg) > 1:
    a = neg.pop()
    b = neg.pop()
    ans += a * b

# 한 개 남았다면 그냥 더함
if pos:
    ans += pos.pop()

# 남은게 있으면 0과 묶음
if neg and zero > 0:
    neg.pop()
    zero -= 1

# 남은 0이 없으면 그냥 더함
if neg:
    ans += neg.pop()

print(ans)