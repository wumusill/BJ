import sys

n = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))

# 오래 걸리는 나무부터 심음
trees.sort(reverse=True)
ans = 0

# 모든 나무가 다 자라는 날짜 갱신
for idx, tree in enumerate(trees):
    ans = max(ans, (idx + tree))

# 나무를 심은 1일이 index 0이라서 + 1
# 다 자라고 그 다음날 이장님 초대 + 1
print(ans + 2)