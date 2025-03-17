N = int(input())
S = input()

if not "p" in S:
    print(S)
    exit()

first_p = S.index("p")

revS = ""
for i in range(N - 1, first_p - 1, -1):
    if S[i] == "p":
        revS += "d"
    else:
        revS += "p"


ret = S
while revS:
    T = S[:first_p] + revS + S[first_p + len(revS) :]
    ret = min(ret, T)
    revS = revS[1:]

print(ret)
