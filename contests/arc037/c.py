
N, K = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

a.sort()
b.sort()

ng, ok = 0, 10**20
while ok - ng > 1:
    m = (ng + ok) // 2
    j = N - 1
    s = 0
    for i in range(N):
        while j >= 0 and a[i] * b[j] > m:
            j -= 1
        s += j + 1

    if s >= K:
        ok = m
    else:
        ng = m

print(ok)
