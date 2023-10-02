import sys

d = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
l = []
sum_hak = 0

for _ in range(20):
    name, hak, grade = sys.stdin.readline().strip().split()
    if grade == 'P':
        continue
    l.append(d[grade] * float(hak))
    sum_hak += float(hak)

score = sum(l) / sum_hak
print(round(score, 6))