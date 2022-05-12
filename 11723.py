import sys

n = int(sys.stdin.readline())
_set = set()
for _ in range(n):
    m = sys.stdin.readline().split()
    if len(m) == 2:
        command = m[0]
        num = int(m[1])
        if command == 'add':
            _set.add(num)
        elif command == 'remove':
            if num in _set:
                _set.remove(num)
            else:
                continue
        elif command == 'check':
            if num in _set:
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            if num in _set:
                _set.remove(num)
            else:
                _set.add(num)
    else:
        command = m[0]
        if command == 'all':
            _set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        else:
            _set.clear()