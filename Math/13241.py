import sys
from math import gcd

a, b = map(int, sys.stdin.readline().split())
_gcd = gcd(a, b)

c = a / _gcd
d = b / _gcd

ans = int(c * d * _gcd)

print(ans)