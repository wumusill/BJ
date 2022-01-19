s = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alpha in croatia:
    s = s.replace(alpha, 'a')

print(len(s))