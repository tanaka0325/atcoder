N = int(input())
L = [x for x in range(1, N + 1) if x % 2 != 0]

ans = 0
for n in L:
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    if cnt == 8:
        ans += 1

print(ans)