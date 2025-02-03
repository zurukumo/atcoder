import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
ab = [[int(i) for i in input().split()] for _ in range(N - 1)]

v = [[] for _ in range(N)]
for i, (a, b) in enumerate(ab) :
    v[a-1].append((b-1, i))
    v[b-1].append((a-1, i))

ret = [0] * (N - 1)

def dfs(pre, cur, color) :
    i = 1
    for nex, j in v[cur] :
        if nex != pre :
            if i == color :
                i += 1
            ret[j] = i
            dfs(cur, nex, i)
            i += 1

dfs(-1, 0, 0)

print(max(ret))
for r in ret :
    print(r)
