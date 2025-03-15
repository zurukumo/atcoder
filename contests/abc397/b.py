S = input()

S = list(S)

last = "i"
ret = 0
while S:
    x = S.pop()
    if x == last:
        ret += 1
    last = x
if last != "i":
    ret += 1
print(ret)
