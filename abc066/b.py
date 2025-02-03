S = input()
S = list(S)

if len(S) % 2 == 0 :
    S.pop()
S.pop()
    
while S :
    if S[:len(S)//2] == S[len(S)//2:] :
        print(len(S))
        break
    S.pop()
    S.pop()