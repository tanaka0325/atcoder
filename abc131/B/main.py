N, L = map(int, input().split())

arr = [L + i for i in range(N)]
arr.sort(key=abs)
print(sum(arr[1:]))
