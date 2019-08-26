N = int(input())
L = list(map(int, input().split()))

arr = [abs(sum(L[i:]) - sum(L[:i])) for i in range(len(L))]
print(min(arr))
