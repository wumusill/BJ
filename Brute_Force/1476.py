E, S, M = map(int, input().strip().split())
e, s, m = 1, 1, 1
ans = 1

while True:
    if e == E and s == S and m == M:
        print(ans)
        break
    e += 1
    s += 1
    m += 1
    ans += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1