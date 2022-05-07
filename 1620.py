import sys

n, m = map(int, sys.stdin.readline().split())
dict_numkey = {}
dict_monkey = {}

for i in range(1, n + 1):
    mon = sys.stdin.readline().strip()
    dict_numkey[i] = mon
    dict_monkey[mon] = i

for _ in range(m):
    t = sys.stdin.readline().strip()
    try:
        print(dict_numkey[int(t)])
    except:
        print(dict_monkey[t])