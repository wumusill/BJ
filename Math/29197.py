import sys

n = int(sys.stdin.readline())

# 기울기로 접근 -> 사분면이 달라도 기울기가 같을 수 있으니 각 사분면별로 분리
# 중복되는 기울기는 알아서 제거되도록 set 사용
quad1 = set()
quad2 = set()
quad3 = set()
quad4 = set()
axis = set()
ans = 0

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    # 각 사분면에 해당하는 기울기 추가
    if x > 0 and y > 0:
        quad1.add(y / x)
    elif x < 0 and y > 0:
        quad2.add(y / x)
    elif x < 0 and y < 0:
        quad3.add(y / x)
    elif x > 0 and y < 0:
        quad4.add(y / x)

    # 축과 일치하는 기울기 추가
    elif x == 0 and y > 0:
        axis.add('y')
    elif x == 0 and y < 0:
        axis.add('-y')
    elif x > 0 and y == 0:
        axis.add('x')
    elif x < 0 and y == 0:
        axis.add('-x')

print(len(quad1) + len(quad2) + len(quad3) + len(quad4) + len(axis))