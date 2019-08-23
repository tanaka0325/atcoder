import sys

N = int(input())
L = list(map(int, input().split()))

n = L[0]
while True:
    if len(L) <= 0:
        break

    if L[0] - n < -1:
        print("No")
        sys.exit()

    n = max(n, L[0])
    L.pop(0)

print("Yes")
