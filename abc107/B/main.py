H, W = map(int, input().split())
L = [list(input()) for _ in range(H)]
L1 = [x for x in L if "#" in x]
L2 = [x for x in zip(*L1) if "#" in x]
for t in zip(*L2):
    print(''.join(t))
