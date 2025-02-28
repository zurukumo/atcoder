n, k = map(int, input().split())
S = input()

S = S * 2
for _ in range(k):
    T = ""
    for i in range(0, len(S), 2):
        a, b = S[i], S[i + 1]
        if a == b:
            T += a
        elif (a, b) in (("R", "S"), ("S", "R")):
            T += "R"
        elif (a, b) in (("S", "P"), ("P", "S")):
            T += "S"
        elif (a, b) in (("P", "R"), ("R", "P")):
            T += "P"
    S = 2 * T

print(S[0])
