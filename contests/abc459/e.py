import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
P = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
D = [int(i) for i in input().split()]


mod = 998244353

vec = [[] for _ in range(N)]
for cur in range(1, N):
    par = P[cur - 1] - 1
    vec[par].append(cur)


ret = 1


def dfs(cur, pre=-1):
    for nex in vec[cur]:
        dfs(nex, cur)

    if D[cur] > C[cur]:
        print("0")
        exit()

    global ret
    for i in range(D[cur]):
        ret = ret * (C[cur] - i) * pow(i + 1, mod - 2, mod) % mod

    if pre != -1:
        C[pre] += C[cur] - D[cur]


dfs(0)
print(ret)
