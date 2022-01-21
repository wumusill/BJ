import sys
input = sys.stdin.readline
#
# n = int(input())
#
# num_list = list(map(int, input().split()))
#
# for num in num_list:
#     while True:
#         if num % 2:
#             break
#         else:
#             print(2, end=' ')
#             num /= 2
#
#     i = 3
#
#     while num > 1:
#         if num % i == 0:
#             print(i, end=' ')
#             num /= i
#         else:
#             i += 2
#     print()

# 시간초과
#####################################################################

# m, n = map(int, input().split())
#
# l = [True] * (n + 1)
#
# l[0] = False
# l[1] = False
#
# for i in range(2, n + 1):
#     if l[i] == True:
#         for j in range(2, n // i + 1):
#             l[i * j] = False
#
# for k in range(len(l)):
#     if l[k] == True and k >= m:
#         print(k)

n = int(input())

num_list = list(map(int, input().split()))

for num in num_list:
    l = [True] * (num + 1)

    l[0] = False
    l[1] = False

    for i in range(2, num + 1):
        if l[i] == True:
            for j in range(2, num // i + 1):
                l[i * j] = False
            if num % i == 0:
                num = num // i
                for _ in range(num // i):
                    print(i, end=' ')

    print()

