S = list(input())
T = list(input())

last = -1
for i in range(len(S)-len(T) + 1) :
    for j in range(len(T)) :
        if S[i+j] != T[j] and S[i+j] != '?' :
            break
    else :
        last = i

if last == -1 :
    print('UNRESTORABLE')
else :
    S[last:last+len(T)] = T[::]
    print(''.join(S).replace('?', 'a'))