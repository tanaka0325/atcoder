A, B = list(map(int, input().split()))

mid = int((max(A, B) - min(A, B)) / 2)
ans = max(A, B) - mid
if abs(A - ans) == abs(B - ans):
    print(ans)
else:
    print("IMPOSSIBLE")
