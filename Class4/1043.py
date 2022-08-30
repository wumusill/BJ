import sys


n, m = map(int, sys.stdin.readline().split())

# 부모를 자기 자신으로 초기화
parent = [i for i in range(n + 1)]
parties = []

# 아는 사람들 기록
know_l = list(map(int, sys.stdin.readline().split()))

# 아는 사람이 0이라면 그냥 파티 수 출력
if len(know_l) == 1:
    print(m)

# 아는 사람이 한 명 이상 있다면
else:
    # 부모를 찾는 함수 재귀는 return 설정이 중요
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # 에러를 유발했던 첫 find 함수 마지막 30줄의 return을 해주지 않아 에러
    # def find(x):
    #     if x == parent[x]:
    #         return parent[x]
    #     parent[x] = find(parent[x])
    #     return parent[x]

    # 부모를 합치는 함수
    def union(x, y):
        x = find(x)
        y = find(y)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y


    # 아는 사람들 부모를 모두 동일하게 처리
    for j in range(1, len(know_l) - 1):
        x = find(know_l[j])
        y = find(know_l[j + 1])
        union(x, y)

    # 파티들 입력
    for _ in range(m):
        party = list(map(int, sys.stdin.readline().split()))[1:]
        parties.append(party)

    # 파티 하나씩 돌면서 한 파티의 부모를 동일하게 처리
    for party in parties:
        for i in range(len(party) - 1):
            x = find(party[i])
            y = find(party[i + 1])
            if x != y:
                union(x, y)

    # 파티 하나씩 돌면서 아는 사람들과 부모가 동일하다면 break
    # 아는 사람이 하나도 없다면 answer += 1
    answer = 0
    for party in parties:
        for person in party:
            if find(person) == find(know_l[1]):
                break
        else:
            answer += 1

    print(answer)


    # print(parent)
# 0
# 9 4
# 1 1
# 4 1 2 3 4
# 3 5 6 7 8
# 2 8 9
# 2 4 9

# 0
# 8 4
# 1 1
# 3 1 2 3
# 3 4 5 6
# 3 6 7 8
# 2 3 8

# 0
# 5 2
# 2 3 4
# 3 4 2 3
# 2 5 3
