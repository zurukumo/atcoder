N = int(input())
S = input()

ret = ""
for s in S:
    c = ord(s)
    c += N
    if c >= 91:
        c = 64 + c - 90
    ret += chr(c)
print(ret)
