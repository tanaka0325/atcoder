N = int(input())
L = [int(input()) for _ in range(N)]
print(int(sum(L) - (max(L) / 2)))
