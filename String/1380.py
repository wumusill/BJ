import sys

cnt = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    d = {}
    for i in range(1, n + 1):
        name = sys.stdin.readline().strip()
        d[i] = [name, 0]
    
    for j in range(n * 2 - 1):
        num, alphabet = sys.stdin.readline().strip().split()
        num = int(num)
        d[num][1] += 1
    
    for k in range(1, n + 1):
        if d[k][1] == 1:
            print(cnt, d[k][0])
            cnt += 1