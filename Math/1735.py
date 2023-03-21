import sys
from math import gcd

# a/b + c/d
a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

# 통분 후 덧셈
# ad/bd + bc/bd = (ad + bc) / bd
a *= d 
a += b * c
b *= d

# 최대 공약수 구해서 약분
res = gcd(a, b)
a /= res
b /= res

print(int(a), int(b))