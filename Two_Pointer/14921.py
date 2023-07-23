import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

left = 0
right = n - 1
ans = 1e9

while left < right:
    # 두 용액 합 계산
    res = l[left] + l[right]

    # 기존값과 새로운 값 중 누가 0에 더 가까운지 계산
    if abs(res) < abs(ans):
        ans = res

    # 계산 후 포인터 갱신
    if res == 0:
        break
    elif res < 0:
        left += 1
    elif res > 0:
        right -= 1

print(ans)