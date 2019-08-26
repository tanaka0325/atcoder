N = int(input())
L = list(map(int, input().split()))

n = L[0]
ans = 0
for i in L:
    if i >= n:
        ans += 1
        n = i

print(ans)
