# print(''.join(map(lambda x: str(10 - int(x)), input())))
print(''.join([str(10 - int(x)) for x in input()]))
