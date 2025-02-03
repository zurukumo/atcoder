S = list(input())
T = list(input())

for i in range(len(S) - 1):
    SS = S[::]
    SS[i], SS[i + 1] = SS[i + 1], SS[i]
    if SS == T:
        print('Yes')
        break
else:
    if S == T:
        print('Yes')
    else:
        print('No')
