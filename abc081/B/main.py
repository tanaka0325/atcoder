n = int(input())
li = list(map(int, input().split()))


def div2(n, cnt=0):
    if n % 2 == 0:
        cnt = cnt + 1
        return div2(n / 2, cnt)
    else:
        return cnt


print(min(list(map(div2, li))))
