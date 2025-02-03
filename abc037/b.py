N, Q = map(int, input().split())

ret = [0] * N

for i in range(Q) :
    L, R, T = map(int, input().split())
    for i in range(L-1, R) :
        ret[i] = T
  
for r in ret :
    print(r)