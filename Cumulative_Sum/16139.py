# 50점, 시간초과
# from collections import Counter
# import sys
#
# strings = list(sys.stdin.readline())
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     s, f_idx, b_idx = sys.stdin.readline().split()
#     d = Counter(strings[int(f_idx):int(b_idx) + 1])
#     print(d[s])

##############################################################################
import sys

word = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())

# ord("a") = 97

answer = [[0] * 26]

# 첫 인덱스에 첫 알파벳 = 1
answer[0][ord(word[0]) - 97] = 1

# 두 번째 인덱스부터 알파벳 개수 업데이트
for i in range(1, len(word)):
    answer.append(answer[-1][:])
    answer[i][ord(word[i]) - 97] += 1

# print(answer)

# 알고 싶은 알파벳, index 두 개 입력 받아 개수 출력
for _ in range(n):
    alphabet, f_idx, b_idx = list(sys.stdin.readline().split())
    f_idx = int(f_idx)
    b_idx = int(b_idx)
    if f_idx == 0:
        print(answer[b_idx][ord(alphabet) - 97])
    else:
        print(answer[b_idx][ord(alphabet) - 97] - answer[f_idx - 1][ord(alphabet) - 97])