import sys

n = int(sys.stdin.readline())
cheese = sys.stdin.readline().split()

quattro = set()
for i in range(n):
    if cheese[i][-6:] == 'Cheese':
        quattro.add(cheese[i])

print('yummy' if len(quattro) > 3 else 'sad')