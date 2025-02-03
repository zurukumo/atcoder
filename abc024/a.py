A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

ret = A*S + B*T
if S + T >= K :
    ret -= (S+T) * C
    
print(ret)