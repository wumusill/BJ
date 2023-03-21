# 528ms

l = [True] * 10001

l[0] = False
l[1] = False

for i in range(2, 10001):
    if l[i] == True:
        for j in range(i*2, 10001, i):
            l[j] = False

m = int(input())

for _ in range(m):
    n = int(input())

    k = n // 2
    for h in range(k, len(l)):
        if l[h] == True and l[n - h] == True:
            print(n-h, h)
            break

# 6024ms
# for _ in range(m):
#     n = int(input())
#     ans_list = []
#
#     for k in range(len(l)):
#         if l[k] == True and l[n-k] == True:
#             ans_list.append((k, n-k))
#
#     if len(ans_list) % 2 == 0:
#         ans = ans_list[:len(ans_list)//2]
#         print(*ans[-1])
#     else:
#         ans = ans_list[:len(ans_list) // 2 + 1]
#         print(*ans[-1])



###########################################################################

# 96ms
# import sys
#
# limit = 10000
# PRIME = [True] * limit
# for i in range(2, limit):
#     if PRIME[i]:
#         for j in range(i+i, limit, i):
#             PRIME[j] = False
#
# T = int(sys.stdin.readline())
# for t in range(T):
#     n = int(sys.stdin.readline())
#     for i in range(n//2, 1, -1):
#         if PRIME[i] and PRIME[n-i]:
#             print( i, n-i )
#             break