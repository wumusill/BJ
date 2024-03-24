import sys


def solution(numbers, visited):
    if len(numbers) == n:
        print(*numbers)
        return

    for i in range(1, n + 1):
        if visited[i]:
            visited[i] = False
            numbers.append(i)
            solution(numbers, visited)
            numbers.pop()
            visited[i] = True


n = int(sys.stdin.readline())
v = [True] * (n + 1)
solution([], v)