N = int(input())
S = [input() for _ in range(N)]

t = {}
ans = 0
for s in S:
    st = "".join(sorted(list(s)))
    if st in t.keys():
        t[st] += 1
        ans += t[st]
    else:
        t[st] = 0

print(ans)
