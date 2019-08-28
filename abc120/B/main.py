A, B, K = map(int, input().split())
L = []

cnt = 0
for i in range(max(A, B), 0, -1):
    if A % i is 0 and B % i is 0:
        cnt += 1
        if cnt is K:
            print(i)
            break