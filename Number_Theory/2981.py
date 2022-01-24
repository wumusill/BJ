

n = int(input())
num_list = []
for _ in range(n):
    num = int(input())
    num_list.append(num)

num_list.sort()

diff = []
for i in range(1, len(num_list)):
    diff.append(num_list[i] - num_list[i-1])

