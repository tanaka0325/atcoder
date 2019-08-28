A, B, C, D = map(int, input().split())

arr = [n for n in range(A, B + 1) if n % C != 0 and n % D != 0]
print(len(arr))
