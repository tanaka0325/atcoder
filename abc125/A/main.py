# A, B, T = map(int, input().split())

# ans = 0
# for i in range(A, T + 1, A):
#     ans += B

# print(ans)

a, b, c = map(int, input().split())
print(c // a * b)
print(c)
print(a * b)
