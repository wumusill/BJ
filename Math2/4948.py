while True:
    n = int(input())
    if n == 0:
        break

    l = [True] * (2*n+1)

    l[0] = False
    l[1] = False

    for i in range(2, n*2+1):
        if l[i]:
            for j in range(i * 2, n*2+1, i):
                l[j] = False

    l_2 = l[n+1:n*2+1]
    print(l_2.count(True))


###########################################################################
# 여러번 연산이 이루어진다는 점 때문에, 범위를 줬으니 큰 배열을 미리 만들어두고 사용하는게 편함

# n보다 크고
def get_b(n):
    end = 2 * n
    count = 0
    is_prime = [True] * (end + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(end ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i + i, end + 1, i):
                is_prime[j] = False

    return is_prime



is_prime_list = get_b(123456)


while True:
    num = int(input())
    if num == 0:
        break

    start, end = num + 1, num * 2
    count = 0
    for i in range(start, end + 1):
        if is_prime_list[i]:
            count += 1
    print(count)