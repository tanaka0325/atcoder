n, a, b = map(int, input().split())

l = []
for i in range(1, n + 1):
    if a <= sum(list(map(int, list(str(i))))) <= b:
        l.append(i)

print(sum(l))
