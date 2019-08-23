import sys

N = int(input())
L = list(map(int, input().split()))
Ls = sorted(L)

cnt = 0
for i in range(N):
    if L[i] != Ls[i]:
        cnt += 1
    if cnt > 2:
        print("NO")
        sys.exit()

print("YES")
