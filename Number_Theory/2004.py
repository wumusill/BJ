import sys
input = sys.stdin.readline()

n, r = map(int, input.split())

cnt_2 = 0
cnt_5 = 0

i = 1
while n // (2 ** i) > 0:
    cnt_2 += n // (2 ** i)
    i += 1

i = 1
while n // (5 ** i) > 0:
    cnt_5 += n // (5 ** i)
    i += 1

i = 1
while r // (2 ** i) > 0:
    cnt_2 -= r // (2 ** i)
    i += 1

i = 1
while r // (5 ** i) > 0:
    cnt_5 -= r // (5 ** i)
    i += 1

i = 1
while (n-r) // (2 ** i) > 0:
    cnt_2 -= (n-r) // (2 ** i)
    i += 1

i = 1
while (n-r) // (5 ** i) > 0:
    cnt_5 -= (n-r) // (5 ** i)
    i += 1


print(min(cnt_2, cnt_5))

#############################################################################
n, m = map(int, input.split())


def countFactor5and2(num):
    count_5 = 0
    i = 5
    while num // i:
        count_5 += num // i
        i *= 5
    count_2 = 0
    i = 2
    while num // i:
        count_2 += num // i
        i *= 2
    return count_2, count_5


counts_nm = countFactor5and2(n - m)
counts_m = countFactor5and2(m)
counts_n = countFactor5and2(n)

total_count = [counts_n[0] - counts_m[0] - counts_nm[0], counts_n[1] - counts_m[1] - counts_nm[1]]

print(min(total_count))