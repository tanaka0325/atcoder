N = int(input())
L = list(map(int, input().split()))

ans = 0
for i in range(N):
    l = sorted(L[i - 1 : i + 2])
    if len(l) != 3:
        continue

    if L[i] == l[1]:
        ans += 1

print(ans)
