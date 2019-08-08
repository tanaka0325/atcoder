n = int(input())
li = list(map(int, input().split()))

li.sort(reverse=True)
alice = sum([li[i] for i in range(len(li)) if i % 2 == 0])
bob = sum([li[i] for i in range(len(li)) if i % 2 != 0])

print(alice - bob)
