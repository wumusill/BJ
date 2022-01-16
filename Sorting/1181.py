n = int(input())
l = []
for _ in range(n):
    word = input()
    if word not in l:
        l.append(word)

for i in range(len(l)):
    l[i] = (l[i], len(l[i]))

sorted_l = sorted(l, key=lambda x: (x[1], x))

for i in sorted_l:
    print(i[0]

###################################################################

import sys

num = int(input())
strList = list(set([sys.stdin.read() for i in range(num)]))
strList.sort()
strList.sort(key=lambda x: len(x))
print(''.join(strList))

####################################################################

from sys import stdin

n = int(stdin.readline())
arr = set()
for i in range(n):
    arr.add(stdin.readline())

new_arr = list(arr)

new_arr.sort()
new_arr.sort(key=lambda x:len(x))

print(''.join(new_arr))