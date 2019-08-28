N = int(input())
L = list(map(int, input().split()))
m = max(L)
print('Yes' if m < sum(L) - m else 'No')
