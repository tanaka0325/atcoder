N = int(input())

for i in range(4, N + 1, 4):
    d = N % i
    if d == 0:
        print("Yes")
        exit()

    if d % 7 == 0:
        print("Yes")
        exit()

for i in range(7, N + 1, 7):
    d = N % i
    if d == 0:
        print("Yes")
        exit()

    if d % 4 == 0:
        print("Yes")
        exit()

print("No")