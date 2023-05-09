import sys

n = int(sys.stdin.readline())
record = set()
ans = 0

for _ in range(n):
    command = sys.stdin.readline().strip()
    if command == 'ENTER':
        record.clear()
    else:
        if command not in record:
            record.add(command)
            ans += 1

print(ans)