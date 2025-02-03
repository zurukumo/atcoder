N, M = map(int, input().split())
disk = [int(input()) for _ in range(M)]

pos = list(range(-1, N))
cur = 0
for nex in disk :
    pos[cur], pos[nex] = pos[nex], pos[cur]
    cur = nex

ret = [0] * N
for i in range(N + 1) :
    if pos[i] != -1 :
        ret[pos[i]] = i
    
for r in ret :
    print(r)