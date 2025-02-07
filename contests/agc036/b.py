import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(i) for i in input().split()]

last = dict()
v = [-1] * N

for i, a in enumerate(A + A):
    if a in last and last[a] < N:
        v[last[a]] = i + 1

    last[a] = i

dist = [-1] * N
cur = 0
cycle = 0
while dist[cur] < 0:
    dist[cur] = cycle
    cycle += v[cur] - cur
    cur = v[cur] % N

NK = N * K

m = NK % cycle
cur = v[cur] % N
s = 0
while m > dist[cur] > 0:
    s = dist[cur]
    cur = v[cur] % N
m -= s

ret = []
seen = set()
for a in A[N - m :]:
    if a in seen:
        p = ret.pop()
        seen.remove(a)
        while p != a:
            seen.remove(p)
            p = ret.pop()
    else:
        ret.append(a)
        seen.add(a)

print(" ".join([str(i) for i in ret]))
