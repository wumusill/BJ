import sys
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    cmd = list(cmd.replace('RR', ''))
    m = int(sys.stdin.readline())
    q = deque(sys.stdin.readline().strip()[1:-1].split(','))
    cnt_R = 0
    breaker = False
    for i in cmd:
        if i == 'R':
            cnt_R += 1
        elif i == 'D':
            if len(q) == 0:
                print('error')
                breaker = True
                break
            if cnt_R % 2 == 0:
                a = q.popleft()
            else:
                a = q.pop()
            if a == '':
                print('error')
                breaker = True
                break
    if breaker == False:
        if cnt_R % 2 == 0:
            print('[' + ','.join(list(q)) + ']')
        else:
            print('[' + ','.join(reversed(list(q))) + ']')
    else:
        continue






# import sys
#
# n = int(sys.stdin.readline())
# for _ in range(n):
#     breaker = True
#     cmd = list(sys.stdin.readline().strip())
#     num = int(sys.stdin.readline())
#     s = sys.stdin.readline().strip()
#     s = s[1: -1]
#     cnt_R = 0
#
#     for i in cmd:
#         if i == 'R':
#             cnt_R += 1
#         else:
#             if cnt_R % 2 == 0:
#                 if len(s) >= 1:
#                     s = s[2:]
#                 else:
#                     print('error')
#                     breaker = False
#                     break
#             else:
#                 if len(s) >= 1:
#                     s = s[:-2]
#                 else:
#                     print('error')
#                     breaker = False
#                     break
#
#     if breaker == True:
#         if cnt_R % 2 == 0:
#             print('[' + s + ']')
#         else:
#             print('[' + s[::-1] + ']')
#     else:
#         continue