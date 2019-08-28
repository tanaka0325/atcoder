N = int(input())
T, A = map(int, input().split())
Hs = list(map(int, input().split()))

arr = [abs(A - (T - Hs[i] * 0.006)) for i in range(N)]
print(arr.index(min(arr)) + 1)
