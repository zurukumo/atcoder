N, Q = map(int, input().split())
A = [int(i) for i in input().split()]
X = [int(input()) for _ in range(Q)]

ret = [0] * Q
Xi = [(x, i) for i, x in enumerate(X)]
Xi.sort()

ls = 0
lc = 0
rs = sum(A)
rc = len(A)
queue = sorted(A, reverse=True)
for x, i in Xi:
    while queue and queue[-1] < x:
        p = queue.pop()
        rs -= p
        rc -= 1
        ls += p
        lc += 1
    ret[i] = x * lc - ls + rs - x * rc

for r in ret:
    print(r)
