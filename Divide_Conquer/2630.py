import sys

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
blue = 0
white = 0


def paper(matrix, n):
    global blue, white
    cnt_0 = 0
    cnt_1 = 0
    for l in matrix:
        cnt_0 += l.count(0)
        cnt_1 += l.count(1)
    if cnt_1 == 0:
        white += 1
        return
    elif cnt_0 == 0:
        blue += 1
        return
    else:
        n //= 2
        matrix_1 = [line[:n] for line in matrix[:n]]
        matrix_2 = [line[n:] for line in matrix[:n]]
        matrix_3 = [line[:n] for line in matrix[n:]]
        matrix_4 = [line[n:] for line in matrix[n:]]
        return paper(matrix_1, n), paper(matrix_2, n), paper(matrix_3, n), paper(matrix_4, n)


paper(matrix, n)
print(white)
print(blue)

# matrix = [
#     [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)],
#     [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)],
#     [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)],
#     [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)],
#     [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)],
#     [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)],
#     [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)],
#     [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)],
# ]
#
# n = 4
#
# matrix_1 = [line[:n] for line in matrix[:n]]
# matrix_2 = [line[n:] for line in matrix[:n]]
# matrix_3 = [line[:n] for line in matrix[n:]]
# matrix_4 = [line[n:] for line in matrix[n:]]
#
# print(matrix_1)
# print(matrix_2)
# print(matrix_3)
# print(matrix_4)