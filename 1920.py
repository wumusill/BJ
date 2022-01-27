import sys
input = sys.stdin.readline

n = int(input())
N = sorted(map(int, input().split()))
m = int(input())
M = map(int, input().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N) - 1
    print(binary(l, N, start, end))