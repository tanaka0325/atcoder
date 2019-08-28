L = [int(input())]
i = 2
while True:
    n = L[-1]
    v = int(n / 2) if n % 2 == 0 else (3 * n) + 1

    if v in L:
        print(i)
        break
    else:
        L.append(v)

    i += 1
