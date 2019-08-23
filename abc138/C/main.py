N = int(input())
L = list(map(float, input().split()))

L.sort()

while True:
    a = L.pop(0)
    b = L.pop(0)
    tmp = (a + b) / 2
    L.append(tmp)
    L.sort()
    if len(L) == 1:
        print(tmp)
        break

