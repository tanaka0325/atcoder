import sys

S = input()

n = ""
for s in S:
    if s == n:
        print("Bad")
        sys.exit()
    n = s

print("Good")
