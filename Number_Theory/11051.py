from math import factorial
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

ans = factorial(n) // (factorial(k) * factorial(n-k))
ans %= 10007
print(ans)


###########################################################################
a, b = map(int, input().split())

up = 1
down = 1
for i in range(a,a-b,-1):
    up *= i

for i in range(1,b+1):
    down *= i

print ((up//down)%10007)