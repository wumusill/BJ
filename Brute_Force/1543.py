import sys

word = sys.stdin.readline().strip()
target = sys.stdin.readline().strip()
cnt = 0

a, b = 0, len(target)
while b <= len(word):
    if word[a:b] == target:
        cnt += 1
        a = b
        b += len(target)
    else:
        a += 1
        b += 1

print(cnt)