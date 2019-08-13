N, Y = map(int, input().split())


def checkEnd(count, rest):
    if count == N and rest == 0:
        return True
    else:
        return False


def main():
    a, m = divmod(Y, 10000)
    if checkEnd(a, m):
        print(a, 0, 0)
        return

    for i in range(a + 1):
        rest = Y - i * 10000
        b, m = divmod(rest, 5000)
        if checkEnd(i + b, m):
            print(i, b, 0)
            return
        for j in range(b + 1):
            rest = Y - i * 10000 - j * 5000
            c, m = divmod(rest, 1000)
            if checkEnd(i + j + c, m):
                print(i, j, c)
                return

    print("-1 -1 -1")


main()
