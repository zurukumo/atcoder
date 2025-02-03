from bisect import bisect_left, bisect_right

S = input()

ret = [0] * len(S)
L = []
R = []
for i, s in enumerate(S) :
    if s == 'L' :
        L.append(i)
    else :
        R.append(-i)

R = R[::-1]
for i, s in enumerate(S) :
    if s == 'L' :
        t = -R[bisect_right(R, -i)]
        if (i - t) % 2 == 0 :
            ret[t] += 1
        else :
            ret[t+1] += 1
    else :
        t = L[bisect_left(L, i)]
        if (t - i) % 2 == 0 :
            ret[t] += 1
        else :
            ret[t-1] += 1
            
print(' '.join(map(str, ret)))
    