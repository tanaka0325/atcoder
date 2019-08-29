N = int(input())
L = [input() for _ in range(N)]

before = L[0]
words = set([before])
for i in range(1, N):
    if before[-1] is not L[i][0] or L[i] in words:
        print("No")
        exit()
    before = L[i]
    words.add(before)

print('Yes')
