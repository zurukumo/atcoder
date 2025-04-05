import bisect

Q = int(input())
A = [int(input()) for _ in range(Q)]


def find_le(a: list[int], x: int):
    i = bisect.bisect_right(a, x)
    if i:
        return a[i - 1]
    return None


M = 10**6 + 10

primes = [0] * M
for i in range(2, M):
    if primes[i] != 0:
        continue
    j = 2
    while i * j < M:
        primes[i * j] += 1
        j += 1

pq = []
for i in range(M):
    if primes[i] == 2:
        pq.append(i * i)

for a in A:
    print(find_le(pq, a))
