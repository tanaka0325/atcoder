N = int(input())
L = [input().split() for _ in range(N)]

ans = 0
for n in L:
    ans += float(n[0]) * 380000.0 if n[1] == 'BTC' else float(n[0])

print(ans)