N, W = map(int, input().split())
STP = [[int(i) for i in input().split()] for _ in range(N)]

imos = [0] * (2 * 10**5 + 10)
for S, T, P in STP:
    imos[S] += P
    imos[T] -= P

for i in range(1, len(imos)):
    imos[i] += imos[i - 1]

if max(imos) <= W:
    print("Yes")
else:
    print("No")
