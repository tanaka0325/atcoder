N, T = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

arr = list(filter(lambda x: x[1] <= T, L))
print(min([x[0] for x in arr]) if arr else 'TLE')
