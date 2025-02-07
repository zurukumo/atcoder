S = input()

o = S[::2]
e = S[1::2]

if o.count("R") + o.count("U") + o.count("D") == len(o) and e.count("L") + e.count(
    "U"
) + e.count("D") == len(e):
    print("Yes")
else:
    print("No")
