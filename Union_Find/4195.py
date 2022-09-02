import sys


n = int(sys.stdin.readline())


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    # 둘의 부모가 같다면 친구 수를 출력
    if x == y:
        print(friend_dic[x])
    # 둘의 부모가 다르다면 더 작은 부모로 통일
    # 부모를 통일하면서 친구 수도 합쳐줌
    # 합쳐진 친구 수 출력
    elif x > y:
        parent[x] = y
        friend_dic[y] += friend_dic[x]
        print(friend_dic[y])
    else:
        parent[y] = x
        friend_dic[x] += friend_dic[y]
        print(friend_dic[x])


for _ in range(n):
    f = int(sys.stdin.readline())

    # 친구 수를 기록하기 위한 dict
    friend_dic = {}
    # 입력 받은 이름을 key 값으로 하여 숫자로 변환하기 위한 dict
    name_dic = {}
    num = 0

    # 부모 초기화, 최악의 경우 친구 관계 두배의 부모 필요
    parent = [i for i in range(f * 2)]

    for _ in range(f):
        friend1, friend2 = sys.stdin.readline().split()

        # dict에 없는 key 값에 그냥 접근하면 KeyError
        # 하지만 get을 이용해 접근하면 존재하지 않는 key 값에 None을 출력
        key_friend1 = name_dic.get(friend1)
        key_friend2 = name_dic.get(friend2)

        # None이라면 존재하지 않는 key 이므로 이름을 숫자로 변환해주고 친구 수는 1로 초기화
        if key_friend1 is None:
            name_dic[friend1] = num
            friend_dic[num] = 1
            num += 1
        if key_friend2 is None:
            name_dic[friend2] = num
            friend_dic[num] = 1
            num += 1

        # 입력된 두 친구의 부모를 union
        union(name_dic[friend1], name_dic[friend2])