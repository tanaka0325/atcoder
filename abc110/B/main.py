N, M, X, Y = map(int, input().split())
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

xs.append(X)
ys.append(Y)
print('No War' if max(xs) < min(ys) else 'War')