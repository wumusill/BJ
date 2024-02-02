import sys


def solution(word1, word2):
    result = 0
    for letter1, letter2 in zip(word1, word2):
        if letter1 != letter2:
            result += 1
    return result


a, b = sys.stdin.readline().split()
answer = int(1e9)

for i in range(0, len(b) - len(a) + 1):
    answer = min(answer, solution(a, b[i:i + len(a)]))

print(answer)