s = input()
S = len(s)

for i in range(S-1) :
    if s[i] == s[i+1] :
        print(i+1, i+2)
        break
    elif i + 2 < S and s[i] == s[i+2] :
        print(i+1, i+3)
        break
else :
    print(-1, -1)