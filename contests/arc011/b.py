N = int(input())
w = input().split()

ret = []
for i in range(N):
    s = ""
    for c in w[i]:
        c = c.lower()
        if c in "bc":
            s += "1"
        elif c in "dw":
            s += "2"
        elif c in "tj":
            s += "3"
        elif c in "fq":
            s += "4"
        elif c in "lv":
            s += "5"
        elif c in "sx":
            s += "6"
        elif c in "pm":
            s += "7"
        elif c in "hk":
            s += "8"
        elif c in "ng":
            s += "9"
        elif c in "zr":
            s += "0"

    if s != "":
        ret.append(s)

print(*ret)
