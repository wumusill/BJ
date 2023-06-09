import sys


sys.setrecursionlimit(10**9)


def recursion(n, cond=True):
    th = 3 ** n
    string = "-" * th
    
    if n == 0:
        if cond == True:
            return string
        else:
            return " "
    if cond == False:
        return " " * th
    return recursion(n - 1) + recursion(n - 1, False) + recursion(n - 1)


inputs = sys.stdin.readlines()

for i in inputs:
    print(recursion(int(i)))

# print(recursion(0))
# print(recursion(1))
# print(recursion(2))
# print(recursion(3))
# print(recursion(4))
# print(recursion(5))
# print(recursion(6))
# print(recursion(7))
# print(recursion(8))
# print(recursion(9))
# print(recursion(10))
# print(recursion(11))
# print(recursion(12))