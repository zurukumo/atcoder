S = input()

while S != "":
    if len(S) >= 5 and S[-5:] == "dream":
        S = S[:-5]
        continue
    if len(S) >= 7 and S[-7:] == "dreamer":
        S = S[:-7]
        continue
    if len(S) >= 5 and S[-5:] == "erase":
        S = S[:-5]
        continue
    if len(S) >= 6 and S[-6:] == "eraser":
        S = S[:-6]
        continue

    break

if S == "":
    print("YES")
else:
    print("NO")
