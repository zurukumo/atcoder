import sys

input = sys.stdin.readline

N = int(input())
vec = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    vec[a - 1].append(b - 1)
    vec[b - 1].append(a - 1)

mod = 10**9 + 7

fac = [1]
for i in range(1, N + 1):
    fac.append(fac[-1] * i % mod)

inv = [pow(fac[-1], mod - 2, mod)]
for i in range(N, 0, -1):
    inv.append(inv[-1] * i % mod)
inv = inv[::-1]


def comb(n, r):
    return fac[n] * inv[n - r] * inv[r] % mod


pattern = [1] * N
subtree = [0] * N

# DFS
stack = [(0, -1, 0)]
while stack:
    cur, pre, op = stack.pop()

    if op == 0:
        stack.append((cur, pre, 1))
        for nex in vec[cur]:
            if nex == pre:
                continue
            stack.append((nex, cur, 0))
    else:
        for nex in vec[cur]:
            pattern[cur] *= (
                pattern[nex] * comb(subtree[cur] + subtree[nex], subtree[nex]) % mod
            )
            pattern[cur] %= mod
            subtree[cur] += subtree[nex]
        subtree[cur] += 1

# BFS
queue = [(0, -1)]
while queue:
    cur, pre = queue.pop()
    for nex in vec[cur]:
        if nex == pre:
            continue
        pattern[nex] = (
            pattern[cur]
            * subtree[nex]
            * inv[N - subtree[nex]]
            * fac[N - subtree[nex] - 1]
            % mod
        )
        queue.append((nex, cur))

for i in range(N):
    print(pattern[i])
