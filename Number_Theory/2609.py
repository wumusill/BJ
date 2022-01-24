from math import gcd
import sys
input = sys.stdin.readline()

m, n = map(int, input.split())
print(gcd(m, n))
print(m * n // gcd(m,n))

########################################################################
a,b = map(int, input.split())
print(math.gcd(a, b))
print(math.lcm(a, b))