from collections import defaultdict

H, W, N = map(int, input().split())

mem = defaultdict(int)
for _ in range(N) :
    a, b = map(int, input().split())
    for i in range(max(2, a-1), min(H-1, a+1)+1) :
        for j in range(max(2, b-1), min(W-1, b+1)+1) :
            mem[(i, j)] += 1
            
ret = [0] * 10
for k, v in mem.items() :
    ret[v] += 1

ret[0] = (H - 2) * (W - 2) - sum(ret)
 
for r in ret :
    print(r)
