from operator import mul

N, M, C = map(int, input().split())
Blist = list(map(int, input().split()))
Alist = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a in Alist:
    if sum(map(lambda x: mul(*x), zip(a, Blist))) + C > 0:
        ans += 1

print(ans)