S = input()

N = len(S)

ret = 0
for i in range(N // 2) :
    if S[i] != S[N-1-i] :
        ret += 1
        
print(ret)