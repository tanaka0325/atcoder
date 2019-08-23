N = int(input())
l = list(map(int, input().split()))

ans = 0.0
for i in l:
    ans += 1 / i


print(1 / ans)

