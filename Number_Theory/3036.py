import sys
from math import gcd

input = sys.stdin.readline
n = int(input())
rings = list(map(int, input().split()))

for i in range(1, n):
    if rings[0] % rings[i] == 0:
        print(str(rings[0] // rings[i]) + '/' + str(1))
    else:
        _gcd = gcd(rings[0], rings[i])
        print(str(rings[0] // _gcd) + '/' + str(rings[i] // _gcd))