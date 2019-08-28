s = int(input())
L = []

while s not in L:
    L.append(s)
    s = int(s / 2) if s % 2 == 0 else (3 * s) + 1

print(len(L) + 1)
