import sys

# 상하 반전
def rotate1(matrix):
    for i in range(len(matrix) // 2):
        matrix[i], matrix[len(matrix) - i - 1] = matrix[len(matrix) - i - 1], matrix[i]
    return matrix

# 시계 방향 90도 회전
def rotate3(matrix, n, m):
    rotated = [[0 for _ in range(n)] for _ in range(m)]
    for x in range(m):
        for y in range(n):
            rotated[x][y] = matrix[n - y - 1][x]
    return rotated

# 반시계 방향 90도 회전
def rotate4(matrix, n, m):
    rotated = [[0 for _ in range(n)] for _ in range(m)]
    for x in range(m):
        for y in range(n):
            rotated[x][y] = matrix[y][m - x - 1]
    return rotated

# 내가 구현한 2번, 시계 방향 90도 회전 후, 상하 반전 후 반시계 방향 90도 회전
# 676ms
def rotate2(matrix):
    temp = rotate3(matrix, len(matrix), len(matrix[0]))
    temp = rotate1(temp)
    return rotate4(temp, len(temp), len(temp[0]))

# 생각보다 간단한 방법이 있었음 : 388ms
def rotate2(matrix):
    return [matrix[i][::-1] for i in range(len(matrix))]


def rotate5_6(matrix, command):
    part1, part2, part3, part4 = [], [], [], []
    for i in range(len(matrix)):
        idx = len(matrix[0]) // 2
        if i < len(matrix) // 2:
            part1.append(matrix[i][:idx])
            part2.append(matrix[i][idx:])
        else:
            part3.append(matrix[i][idx:])
            part4.append(matrix[i][:idx])

    rotated = []
    if command == 5:
        for a, b in zip(part4, part1):
            rotated.append((a + b))
        for a, b in zip(part3, part2):
            rotated.append((a + b))
    else:
        for a, b in zip(part2, part3):
            rotated.append((a + b))
        for a, b in zip(part1, part4):
            rotated.append((a + b))

    return rotated


n, m, r = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
commands = list(map(int, sys.stdin.readline().split()))

for command in commands:
    if command == 1:
        matrix = rotate1(matrix)
    elif command == 2:
        matrix = rotate2(matrix)
    elif command == 3:
        matrix = rotate3(matrix, len(matrix), len(matrix[0]))
    elif command == 4:
        matrix = rotate4(matrix, len(matrix), len(matrix[0]))
    elif command == 5:
        matrix = rotate5_6(matrix, 5)
    elif command == 6:
        matrix = rotate5_6(matrix, 6)

for arr in matrix:
    print(*arr)