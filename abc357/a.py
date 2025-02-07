N, M = map(int, input().split())
H = [int(i) for i in input().split()]

s = 0
for i, h in enumerate(H):
    s += h
    if s > M:
        print(i)
        exit()
print(N)
