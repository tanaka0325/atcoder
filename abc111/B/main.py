N = int(input())
L = [int(str(x) * 3) for x in range(1, 10)]

for n in L:
    if N <= n:
        print(n)
        break