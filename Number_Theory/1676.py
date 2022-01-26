from math import factorial

n = int(input())
num = factorial(n)
l = reversed(list(str(num)))
ans = 0
for i in l:
    if i == '0':
        ans += 1
    else:
        break

print(ans)