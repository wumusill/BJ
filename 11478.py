import sys

word = sys.stdin.readline()
ans_set = set()

for i in range(len(word)):
    for j in range(i, len(word)):
        ans_set.add(word[i:j])

print(len(ans_set) - 1)