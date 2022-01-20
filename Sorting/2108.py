import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

l.sort()
cnt = Counter(l).most_common()
cnt_l = [i[0] for i in cnt if cnt[0][1] == i[1]]
cnt_l.sort()

print(round(sum(l) / len(l)))
print(l[len(l)//2])
print(cnt_l[1] if len(cnt_l) > 1 else cnt_l[0] )
print(max(l) - min(l))