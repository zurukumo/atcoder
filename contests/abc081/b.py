N = int(input())
A = [int(i) for i in input().split()]

m = float("inf")
for a in A:
    c = 0
    while a % 2 == 0:
        a //= 2
        c += 1
    m = min(m, c)

print(m)
