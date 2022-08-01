import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
matA = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

m, k = map(int, sys.stdin.readline().rstrip().split())
matB = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]

ans_mat = []

for i in range(n):#3
    ans_l = []
    for x in range(k):#3
        res = 0
        for y in range(m):#3
            res += matA[i][y] * matB[y][x]
        ans_l.append(res)
    ans_mat.append(ans_l)

for l in ans_mat:
    print(*l)