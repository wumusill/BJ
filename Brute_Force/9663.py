import sys

n = int(sys.stdin.readline())
queen = [0] * 15
count = 0


def dfs(queen, n, row):
    global count
    if n == row:
        count += 1
        return

    for x in range(n):
        queen[row] = x
        for y in range(row):
            if queen[y] == queen[row]:
                break
            if abs(queen[row] - queen[y]) == abs(row - y):
                break
        else:
            dfs(queen, n, row + 1)


dfs(queen, n, 0)
print(count)