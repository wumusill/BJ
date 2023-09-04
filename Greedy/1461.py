# 가장 멀리 갈 때 최대한 많은 책을 가지고 간다. 그리고 다시 돌아올 필요 없기 때문에 += max * 1
# 그 다음도 역시 가장 멀리 갈 때 최대한 많은 책을 가지고 간다. 그러나 다시 돌아와야 하기 때문에 += max * 2
# 음수와 양수 나눠서 생각, 절댓값이 가장 큰 원소를 가지고 있는 부호 먼저 진행
import sys

n, m = map(int, sys.stdin.readline().split())
l = sorted(map(int, sys.stdin.readline().split()))
ans = 0

# flag의 역할 : 돌아와야 하는지 아닌지 판단
flag = True

# 정리할 책이 m보다 적거나 같아질 때까지 반복문으로 정리 수행
while len(l) > m:
    left, right = abs(l[0]), abs(l[-1])
    if flag:                                            # 처음엔 안돌아와도 됨
        if left > right:
            ans += abs(left)                            # 안돌아와도 될 때는 += abs(max(left, right)) * 1
            l = l[m:]                                   # 정리한 책 리스트에서 제거
        else:
            ans += abs(right)
            l = l[:len(l) - m]
        flag = False                                    # 다음엔 무조건 돌아올 수 있도록 처리
    else:
        if left > right:
            ans += abs(left) * 2                        # 돌아와야 할 때는 += abs(max(left, right)) * 2
            l = l[m:]
        else:
            ans += abs(right) * 2
            l = l[:len(l) - m]

# 위 while 문을 통과하지 않고 처음부터 주어진 책의 개수가 m보다 작을 때 -> 한 번 안돌아와도 됨
# 처음과 마지막 원소의 부호가 다르다면 한쪽은 반드시 갔다가 돌아와야함
left, right = abs(l[0]), abs(l[-1])

if flag:
    # 절댓값이 더 작은 쪽을 갔다가 돌아오는 것이 유리
    # 양쪽 절댓값이 같으면 어느 쪽을 다녀와도 상관 없음
    if l[0] * l[-1] < 0:
        ans += max(left, right)
        ans += min(left, right) * 2
    # 부호가 같다면 그냥 한 번에 정리
    else:
        ans += max(left, right)

# 위 while 문을 통과해서 책의 개수가 m보다 작아졌을 때 -> 무조건 돌아와야 함
# 부호가 다르면 양쪽 다 돌아와야 함
# 부호가 같으면 한쪽만 갔다 오면 됨
else:
    if l[0] * l[-1] < 0:
        ans += right * 2
        ans += left * 2
    else:
        ans += max(left, right) * 2

print(ans)


# 4 2
# 10 50 -30 -40
# 130

# 47 27
# -4599 -1950 -6837 8627 527 2752 9764 3914 -4049 -267 1054 -3512 8100 -7003 -7641 -2211 -6207 4312 -2563 4872 -9471 2913 -7907 -654 3463 -2717 -5152 -7093 1692 944 -1057 -1629 -4176 9634 6209 -2684 -7103 -1507 -579 6883 6055 6043 6732 -3934 -3551 565 8326
# 28706

