import sys

n = int(sys.stdin.readline())
l = sorted(map(int, sys.stdin.readline().split()))

ans = 0

# target 순회
for target_idx in range(n):
    # 양 끝에서 투 포인터 시작
    left, right = 0, n - 1
    while left < right:
        res = l[left] + l[right]
        target = l[target_idx]

        # 만약 타겟과 포인터가 같으면 건너 뛰는 조건문
        if target_idx == left:
            left += 1
            continue
        elif target_idx == right:
            right -= 1
            continue

        # target과 투 포인터의 합을 비교하는 조건문
        if res == target:
            ans += 1
            break
        elif res < target:
            left += 1
        elif res > target:
            right -= 1


print(ans)


# 4
# 0 0 0 0
# 4

# 5
# -1 -2 0 -1 -2 -> [-2, -2, -1, -1, 0]
# 4

# 5
# 0 0 0 0 1 -> [0, 0, 0, 0, 1]
# 4