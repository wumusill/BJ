import sys

pos = True
n = sorted(map(int, list(sys.stdin.readline().strip())), reverse=True)

if n[-1] != 0:
    pos = False
elif sum(n) % 3 != 0:
    pos = False

if pos:
    print(int(''.join(map(str, n))))
else:
    print(-1)