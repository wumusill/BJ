s = input().upper()
element = set(s)
cnt = {}

for i in element:
    cnt[i] = s.count(i)

l = sorted(cnt.items(), reverse=True, key= lambda item : item[1])

if len(l) == 1:
    print(l[0][0])
else:
    if l[0][1] == l[1][1]:
        print('?')
    else:
        print(l[0][0])