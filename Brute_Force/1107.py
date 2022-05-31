import sys
from itertools import product

target_num = sys.stdin.readline().strip()
num_l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if target_num == '100':
    print(0)
else:
    cnt_error_num = int(sys.stdin.readline())
    if cnt_error_num == 0:
        print(min(len(target_num), abs(int(target_num) - 100)))
    else:
        error_num = list(map(int, sys.stdin.readline().split()))
        for i in error_num:
            num_l.remove(i)
        _max = -int(1e9)
        _min = int(1e9)
        for i in range(len(target_num) - 1, len(target_num) + 2):
            if i == 0:
                continue
            nPir = product(map(str, num_l), repeat=i)
            case_list = set(nPir)
            for case in case_list:
                made_num = int(''.join(case))
                if made_num >= int(target_num):
                    _min = min(_min, made_num)
                elif made_num <= int(target_num):
                    _max = max(_max, made_num)

        a = abs(_min - int(target_num)) + len(str(_min))
        b = abs(int(target_num) - _max) + len(str(_max))
        c = abs(100 - int(target_num))
        print(min(a, b, c))