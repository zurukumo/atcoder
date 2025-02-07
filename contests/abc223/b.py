S = input()

mi = S
ma = S
for i in range(len(S)):
    mi = min(mi, S[i:] + S[:i])
    ma = max(ma, S[i:] + S[:i])

print(mi)
print(ma)
