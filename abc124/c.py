S = input()

s1, s2 = 0, 0
for i, s in enumerate(S) :
    if i % 2 != int(s) :
        s1 += 1
    else :
        s2 += 1

print(min(s1, s2))