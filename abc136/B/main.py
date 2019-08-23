N = input()

ans = 0
for i in range(1, len(N)):
    if i % 2 != 0:
        ans += 9 * 10 ** (i - 1)

if len(N) % 2 != 0:
    ans += int(N) - 10 ** (len(N) - 1) + 1

print(ans)
