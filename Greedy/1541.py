l = input().split('-')

if len(l) == 1:     # - 가 없을 경우
    print(sum(map(int, l[0].split('+'))))

else:
    if '+' in l[0]:     # 첫 수식이 +일 경우
        answer = sum(map(int, l[0].split('+')))
    else:
        answer = int(l[0])

    for i in range(1, len(l)):
        if '+' in l[i]:
            answer -= sum(map(int, l[i].split('+')))
        else:
            answer -= int(l[i])

    print(answer)