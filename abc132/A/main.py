S = input()
L = sorted(list(S))

if L[0] == L[1] and L[2] == L[3] and L[1] != L[2]:
    print("Yes")
else:
    print("No")
