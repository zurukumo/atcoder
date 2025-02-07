n, X = map(int, input().split())
a = [int(i) for i in input().split()]

res = 0
i = 0
while X > 0:
    if X & 1:
        res += a[i]
    i += 1
    X >>= 1

print(res)
