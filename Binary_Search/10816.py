import sys
from collections import Counter

n = int(input())
card = sys.stdin.readline().split()

m = int(input())
ans_card = sys.stdin.readline().split()

C = Counter(card)

for i in ans_card:
    if i in C:
        print(C[i], end=' ')
    else:
        print(0, end=' ')