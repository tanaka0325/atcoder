N = int(input())
S = [(i, tuple(input().split())) for i in range(1, N + 1)]

arr = sorted(S, key=lambda item: int(item[1][1]), reverse=True)
arr2 = sorted(arr, key=lambda item: item[1][0])

for item in arr2:
    print(item[0])

