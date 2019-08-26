N, X = map(int, input().split())
L = list(map(int, input().split()))

ans = 1
distance = 0
for n in L:
    distance = distance + n
    if distance <= X:
        ans += 1
    else:
        break

print(ans)
