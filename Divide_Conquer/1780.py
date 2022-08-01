import sys

n = int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans_m1 = 0
ans_0 = 0
ans_p1 = 0


def num_paper(mat, n):
    global ans_m1, ans_0, ans_p1
    cnt_m1 = 0
    cnt_0 = 0
    cnt_p1 = 0
    for row in mat:
        cnt_m1 += row.count(-1)
        cnt_0 += row.count(0)
        cnt_p1 += row.count(1)
    if cnt_m1 == 0 and cnt_0 == 0:
        ans_p1 += 1
    elif cnt_m1 == 0 and cnt_p1 == 0:
        ans_0 += 1
    elif cnt_p1 == 0 and cnt_0 == 0:
        ans_m1 += 1
    else:
        n //= 3
        mat_1 = list()
        mat_2 = list()
        mat_3 = list()
        mat_4 = list()
        mat_5 = list()
        mat_6 = list()
        mat_7 = list()
        mat_8 = list()
        mat_9 = list()
        for l in mat[:n]:
            mat_1.append(l[:n])
            mat_2.append(l[n:n * 2])
            mat_3.append(l[n * 2:n * 3])
        for l in mat[n:n * 2]:
            mat_4.append(l[:n])
            mat_5.append(l[n:n * 2])
            mat_6.append(l[n * 2:n * 3])
        for l in mat[n * 2:n * 3]:
            mat_7.append(l[:n])
            mat_8.append(l[n:n * 2])
            mat_9.append(l[n * 2:n * 3])

        return num_paper(mat_1, n), num_paper(mat_2, n), num_paper(mat_3, n), \
               num_paper(mat_4, n), num_paper(mat_5, n), num_paper(mat_6, n), \
               num_paper(mat_7, n), num_paper(mat_8, n), num_paper(mat_9, n)


num_paper(mat, n)

print(ans_m1)
print(ans_0)
print(ans_p1)