S = input()

ans = 753
for i in range(len(S)):
    X = int(S[i:i + 3]) - 753
    if abs(X) < ans:
        ans = abs(X)
print(ans)