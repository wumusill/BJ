import sys

n = int(sys.stdin.readline())
company = set()

for _ in range(n):
    name, action = sys.stdin.readline().strip().split()
    if action == "enter":
        company.add(name)
    elif action == "leave":
        company.remove(name)

for name in sorted(company, reverse=True):
    print(name)