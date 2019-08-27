import math

L = [int(input()) for i in range(5)]

total = 0
sub = 0
for i in L:
    if i % 10 == 0:
        total += i
    else:
        rest = 10 - (i % 10)
        if rest > sub:
            sub = rest
        total += math.ceil(i / 10) * 10

print(total - sub)
