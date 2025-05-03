Q = int(input())
TS = [input().split() for _ in range(Q)]


trie = {}

mod1 = (1 << 61) - 1
mod2 = (1 << 31) - 1


def insert(S, v):
    k1 = 0
    k2 = 0
    for c in S:
        k1 = (k1 * 27 + ord(c) - ord("a") + 1) % mod1
        k2 = (k2 * 27 + ord(c) - ord("a") + 1) % mod2
    if (k1, k2) not in trie:
        trie[(k1, k2)] = v


def query(S):
    k1 = 0
    k2 = 0
    v = float("inf")
    for c in S:
        k1 = (k1 * 27 + ord(c) - ord("a") + 1) % mod1
        k2 = (k2 * 27 + ord(c) - ord("a") + 1) % mod2
        if (k1, k2) in trie:
            v = min(v, trie[(k1, k2)])
    return v


for i, (T, S) in enumerate(TS):
    if T == "1":
        insert(S, i)

imos = [0] * (Q + 1)
for i, (T, S) in enumerate(TS):
    if T == "2":
        imos[i] += 1
        midx = max(i, query(S))
        if midx != float("inf"):
            imos[midx] -= 1


for i in range(1, Q + 1):
    imos[i] += imos[i - 1]

for r in imos[:-1]:
    print(r)
