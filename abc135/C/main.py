N = int(input())
M = list(map(int, input().split()))
U = list(map(int, input().split()))

ans = 0
for i in range(N):
    m = M[i] + M[i + 1] - U[i]
    if m > 0:
        ans += U[i]
        M[i + 1] = min(m, M[i + 1])
    else:
        ans += M[i] + M[i + 1]
        M[i + 1] = 0

print(ans)
