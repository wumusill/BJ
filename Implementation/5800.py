import sys

n = int(sys.stdin.readline())


def solution():
    l = list(map(int, sys.stdin.readline().split()))
    scores = l[1:]
    scores.sort(reverse=True)

    gap = 0
    for i in range(1, l[0]):
        gap = max(gap, scores[i - 1] - scores[i])

    return scores[0], scores[-1], gap


for class_num in range(1, n + 1):
    mx, mn, gap = solution()
    print(f"Class {class_num}")
    print(f"Max {mx}, Min {mn}, Largest gap {gap}")