import sys

t = int(sys.stdin.readline())

# 에라토스테네스의 체
prime = [True] * 1000001
prime[0] = False
prime[1] = False

for i in range(int(1000001 ** 0.5 + 1)):
    if prime[i]:
        for j in range(i * 2, 1000001, i):
            prime[j] = False

# 입력값으로 연산
for _ in range(t):
    n = int(sys.stdin.readline())
    ans = 0

    # 순서만 다른 것은 같은 파티션
    for i in range(2, n // 2 + 1):
        if prime[i] and prime[n - i]:
            ans += 1
    print(ans)

# 1
# 1000000
# 5402