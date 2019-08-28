N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
ALL = sum(list(map(lambda x: x[1:], L)), [])

ans = 0
for i in set(ALL):
    if ALL.count(i) is N:
        ans += 1

print(ans)
