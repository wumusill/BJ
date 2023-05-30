# 1/3의 경우 소수점 아래 3을 무한대로 출력하지 않는다.
# 따라서 내가 원하는 자릿수의 숫자를 알기 위해선 직접 계산해야 한다.
import sys

a, b, n = map(int, sys.stdin.readline().split())
l = []

# divmod : (몫, 나머지)를 구해주는 함수
div, mod = divmod(a, b)
l.append((div, mod))

# n번째 자리 숫자를 알고 싶으므로 n + 1번 반복문 수행해야 함
# 하지만 위에서 한 번 수행했으므로 n번 수행해도 됨
for _ in range(n):
    # 나머지에 10을 곱하고 인수로 한 번 더 나누기
    div, mod = divmod(mod * 10, b)
    # 몫과 나머지 기록
    l.append((div, mod))

# n번째 자리의 몫 출력
print(l[n][0])