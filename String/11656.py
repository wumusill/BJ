import sys

s = sys.stdin.readline().strip()
l = sorted([s[i:] for i in range(len(s))])
for ans in l:
    print(ans)