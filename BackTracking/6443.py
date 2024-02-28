# 입력받은 단어내에 몇몇 철자가 중복될 수 있다. 이 경우 같은 단어가 여러 번 만들어 질 수 있는데, 한 번만 출력해야 한다.
# 또한 출력할 때에 알파벳 순서로 출력해야 한다.
import sys


def solution(alphabet, now):
    if len(now) == len(word):
        print(now)
        return

    for i in alphabet:
        if alphabet[i]:
            alphabet[i] -= 1
            solution(alphabet, now + i)
            alphabet[i] += 1


n = int(sys.stdin.readline())
for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    word.sort()

    alphabet = {}
    for i in word:
        if i in alphabet:
            alphabet[i] += 1
        else:
            alphabet[i] = 1

    solution(alphabet, '')