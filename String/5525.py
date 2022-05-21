import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()

word = 'IOI'
ans, count = 0, 0
idx = 0

while idx < m - 1:
    if s[idx:idx + 3] == word:
        count += 1
        idx += 2
        if count == n:
            ans += 1
            count -= 1
    else:
        count = 0
        idx += 1

print(ans)