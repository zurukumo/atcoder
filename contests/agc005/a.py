X = input()

S, T = 0, 0
for x in X:
    if x == "T" and S > 0:
        S -= 1
    elif x == "T":
        T += 1
    elif x == "S":
        S += 1

print(S + T)
