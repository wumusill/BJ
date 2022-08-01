import sys

n = int(sys.stdin.readline())
matrix = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
ans_list = []


def solution(n, matrix):
    n = n // 2
    cnt_0 = 0
    cnt_1 = 0
    for list in matrix:
        for num in list:
            if num == 0:
                cnt_0 += 1
            else:
                cnt_1 += 1
    if cnt_1 == 0:
        ans_list.append("0")
        return
    elif cnt_0 == 0:
        ans_list.append("1")
        return
    else:
        ans_list.append("(")
        matrix_1 = [list[:n] for list in matrix[:n]]
        matrix_2 = [list[n:] for list in matrix[:n]]
        matrix_3 = [list[:n] for list in matrix[n:]]
        matrix_4 = [list[n:] for list in matrix[n:]]
        return solution(n, matrix_1), solution(n, matrix_2), \
               solution(n, matrix_3), solution(n, matrix_4), ans_list.append(")")


solution(n, matrix)

print(''.join(ans_list))