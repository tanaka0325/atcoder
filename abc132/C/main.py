N = int(input())
L = sorted(list(map(int, input().split())))

i = int(N / 2)
print(L[i] - (L[i - 1]))
