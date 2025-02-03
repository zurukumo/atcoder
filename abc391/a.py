D = input()

ret = ""

for c in D:
    if c == "N":
        ret += "S"
    elif c == "S":
        ret += "N"
    elif c == "E":
        ret += "W"
    elif c == "W":
        ret += "E"

print(ret)
