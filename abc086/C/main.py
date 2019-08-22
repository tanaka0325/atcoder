N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]


def check(before, after):
    steps = after[0] - before[0]
    distance_sub = (after[1] + after[2]) - (before[1] + before[2])

    if steps < distance_sub or (steps % 2 == 0) != (distance_sub % 2 == 0):
        return False

    return True


def main():
    for i in range(N):
        if i == 0:
            if not check([0, 0, 0], L[i]):
                print("No")
                return
        else:
            if not check(L[i - 1], L[i]):
                print("No")
                return
    print("Yes")


main()
