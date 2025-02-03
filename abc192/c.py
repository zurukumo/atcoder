N, K = input().split()
K = int(K)

a = N
for _ in range(K):
    a = [i for i in a]
    a.sort()
    a = "".join(a)
    g1 = int(a)
    g2 = int(a[::-1])
    a = str(g2 - g1)

print(a)
