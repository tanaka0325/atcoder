import time

start = time.time()

a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0
rest = x

max500 = min(int(rest / 500), a)
for i in range(max500 + 1):
    rest = x - (500 * i)
    if rest == 0:
        cnt = cnt + 1
        continue

    max100 = min(int(rest / 100), b)
    for j in range(max100 + 1):
        rest = x - (500 * i) - (100 * j)
        if rest == 0:
            cnt = cnt + 1
            continue

        max50 = min(int(rest / 50), c)
        for k in range(max50 + 1):
            rest = x - (500 * i) - (100 * j) - (50 * k)
            if rest == 0:
                cnt = cnt + 1
                continue

print(cnt)

elapsed_time = time.time() - start
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

