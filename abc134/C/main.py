N = int(input())
L = [int(input()) for _ in range(N)]

Ls = sorted(L, reverse=True)
for i in range(N):
    if L[i] == Ls[0]:
        print(Ls[1])
    else:
        print(Ls[0])
