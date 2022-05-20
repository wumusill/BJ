import sys

n, m = map(int, sys.stdin.readline().split())
memo = {}

for _ in range(n):
    address, password = sys.stdin.readline().split()
    memo[address] = password

for _ in range(m):
    address = sys.stdin.readline().strip()
    print(memo[address])