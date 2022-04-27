import sys

n, m = map(int, sys.stdin.readline().split())
sum_matrix = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        sum_matrix[i + 1][j + 1] = sum_matrix[i + 1][j] + sum_matrix[i][j + 1] - sum_matrix[i][j] + l[j]

for t in range(m):
    x_1, y_1, x_2, y_2 = map(int, sys.stdin.readline().split())
    ans = sum_matrix[x_2][y_2] - (sum_matrix[x_1 - 1][y_2] + sum_matrix[x_2][y_1 - 1]) + sum_matrix[x_1 - 1][y_1 - 1]
    print(ans)



# l = [
#     [1, 2],
#     [3, 4]
# ]

# l = [
#     [0, 0, 0],
#     [0, 1, 3],
#     [0, 4, 10]
# ]