S1 = input()
S2 = input()
S3 = input()
T = input()

ret = ""
for c in T:
    if c == "1":
        ret += S1
    elif c == "2":
        ret += S2
    else:
        ret += S3
print(ret)
