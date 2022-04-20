# 설탕 배달
# 5로 나누어 떨어지면 몫이 정답
# 나누어 떨어지지 않는다면 3을 빼고 ans += 1 한다음 다시 5로 나눠보기를 반복
# n이 음수가 되면 -1 출력

n = int(input())

ans = 0
while True:
    if n < 0:
        ans = -1
        print(ans)
        break
    if n % 5 == 0:
        ans = ans + (n // 5)
        print(ans)
        break
    else:
        n -= 3
        ans += 1