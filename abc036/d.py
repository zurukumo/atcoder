import sys

sys.setrecursionlimit(10**5)

N = int(input())

v = [[] for _ in range(N)]
for _ in range(N-1) :
    a, b = map(int, input().split())
    v[a-1].append(b-1)
    v[b-1].append(a-1)

MOD = 10 ** 9 + 7

def mul(x) :
    ret = 1
    for x_ in x :
        ret *= x_
        ret %= MOD
    return ret

def bfs(cur, par) :
    children1 = [] #子の全ての組み合わせ
    children2 = [] #子が白の組み合わせ
    
    for nex in v[cur] :
        if nex == par :
            continue
        W, B = bfs(nex, cur)
        children1.append(W+B)
        children2.append(W)
        
    return (mul(children1), mul(children2))
    
print(sum(bfs(0, -1)) % MOD)
        