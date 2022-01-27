import sys

n = int(input())
l = []
for order in range(n):
    age, name = sys.stdin.readline().split()
    l.append((age, name, order))

l.sort(key= lambda x: (int(x[0]), int(x[2])))

for i in l:
    print(*i[:2])