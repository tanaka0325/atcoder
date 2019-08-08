n, a, b = map(int, input().split())

l = []
for i in range(1, n + 1):
    if len(str(i)) == 1:
        if i >= a and i <= b:
            l.append(i)
    else:
        li = [int(str(i)[j]) for j in range(len(str(i)))]
        if sum(li) >= a and sum(li) <= b:
            l.append(i)

print(sum(l))
