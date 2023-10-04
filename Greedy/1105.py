# 왼쪽이 무조건 작은 수 : a <= x <= b
# 자릿수가 다르면 8이 하나도 없는 번호를 만들 수 있음
# 자릿수가 같을 때
    # 앞자리 수부터 확인
        # 둘 다 같은 수면 그 다음 자릿수로 확인
        # 근데 8이면 무조건 8을 써야하므로 ans += 1
    # 서로 다른 숫자면 그 뒤부터는 8을 사용하지 않고 숫자를 만들 수 있으므로 break
import sys

a, b = sys.stdin.readline().strip().split()
ans = 0

if len(a) != len(b):
    print(ans)
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            if a[i] == '8' and b[i] == '8':
                ans += 1
        else:
            break
    print(ans)


# 88 98
# 0

# 1887 1888
# 2