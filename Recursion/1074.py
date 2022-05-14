import sys

n, r, c = map(int, sys.stdin.readline().split())
k = 2 ** n
num = k ** 2


def solution(num, k, r, c):
    if k == 2:
        ans = 0
        if r == 0 and c == 0:
            ans = num - 4
        elif r == 0 and c == 1:
            ans = num - 3
        elif r == 1 and c == 0:
            ans = num - 2
        elif r == 1 and c == 1:
            ans = num - 1
        print(ans)
        return
    else:
        k //= 2
        if r < k and c < k:
            return solution(num - (k ** 2) * 3, k, r % k, c % k)
        elif r < k and c >= k:
            return solution(num - (k ** 2) * 2, k, r % k, c % k)
        elif r >= k and c < k:
            return solution(num - (k ** 2) * 1, k, r % k, c % k)
        elif r >= k and c >= k:
            return solution(num - (k ** 2) * 0, k, r % k, c % k)


solution(num, k, r, c)