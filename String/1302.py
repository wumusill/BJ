import sys

n = int(sys.stdin.readline())
d = {}

for _ in range(n):
    title = sys.stdin.readline()
    if title in d:
        d[title] += 1
    else:
        d[title] = 1

d = sorted(d.items(), key=lambda item:(-item[1], item[0]))
print(d[0][0])