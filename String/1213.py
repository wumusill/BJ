import sys
from collections import deque

string = sys.stdin.readline().strip()
l = list(string)
d = {}

# 알파벳 개수 기록
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

# 개수가 홀수인 알파벳이 2개 이상 있으면 펠린드롬 불가능
# 홀수가 한개라면 한개를 가운데에 추가
# 나머지 알파벳은 사전 역순으로 앞뒤로 삽입
odd = []
even = []
for i in d:
    if d[i] % 2 == 1:
        odd.append(i)
    else:
        even.append(i)

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    q = deque()
    if odd:
        q.append(odd[0])
        d[odd[0]] -= 1

    d = sorted(d.items(), key=lambda item: item[0], reverse=True)

    for key, val in d:
        for _ in range(val // 2):
            q.append(key)
            q.appendleft(key)

    print(''.join(q))