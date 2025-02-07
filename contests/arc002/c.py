N = int(input())
c = input()

LR = [
    "AA",
    "AB",
    "AX",
    "AY",
    "BA",
    "BB",
    "BX",
    "BY",
    "XA",
    "XB",
    "XX",
    "XY",
    "YA",
    "YB",
    "YX",
    "YY",
]

ret = float("inf")
for l in range(16):
    d = c.replace(LR[l], "L")
    for r in range(16):
        ret = min(ret, len(d) - d.count(LR[r]))

print(ret)
