S = input()
T = input()

if S == T:
    print(0)
    exit()

i = 0
while i < len(S) and i < len(T):
    if S[i] == T[i]:
        i += 1
    else:
        break

print(i + 1)
