K, X = map(int, input().split())
s = X - (K - 1)

ans = [str(n) for n in range(s, (X + K))]
print(" ".join(ans))
