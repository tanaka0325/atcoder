N = int(input())
Vs = list(map(int, input().split()))
Cs = list(map(int, input().split()))

ans = 0
for i in range(N):
    if Vs[i] - Cs[i] > 0:
        ans += Vs[i] - Cs[i]

print(ans)
