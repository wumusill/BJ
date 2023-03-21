t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    apart = [i for i in range(n + 1)]
    for i in range(k):
        apart[-1] = sum(apart)
        for j in range(-2, -(n + 1), -1):
            apart[j] = sum(apart[:j + 1])

    print(apart[n])