r, D, x = map(int, input().split())


def f(i, b):
    if i > 10:
        return

    y = r * b - D
    print(y)
    i += 1
    f(i, y)


f(1, x)
