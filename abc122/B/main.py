S = input()
L = ["A", "C", "G", "T"]

arr = []
st = ""

for s in S:
    if st and s not in L:
        st = ""
    if s in L:
        st += s
        arr.append(st)

print(max(map(len, arr)) if arr else 0)
