m, n = map(int, input().split())

l = [True] * (n+1)

l[0] = False
l[1] = False

for i in range(2, n+1):
    if l[i] == True:
        for j in range(2, n//i + 1):
            l[i * j] = False

for k in range(len(l)):
    if l[k] == True and k >= m:
        print(k)