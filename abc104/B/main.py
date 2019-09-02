S = input()

if S[0] != 'A':
    print('WA')
    exit()

if S[2:-1].count('C') != 1:
    print('WA')
    exit()

i = S[2:-1].find('C')

if i >= 0:
    S = S[1:2 + i] + S[2 + i + 1:]
    if S.islower():
        print('AC')
        exit()
    else:
        print('WA')
        exit()
else:
    print('WA')