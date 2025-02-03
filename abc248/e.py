from collections import defaultdict

N, K = map(int, input().split())
XY = [[int(i) for i in input().split()] for _ in range(N)]

comb = defaultdict(int)

if K == 1:
    print("Infinity")
    exit()

for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = XY[i]
        x2, y2 = XY[j]

        if x2 - x1 == 0:
            counter = 0
            for x3, y3 in XY:
                if x3 == x1:
                    counter += 1
            if counter >= K:
                comb[counter] += 1
        else:
            counter = 0
            for x3, y3 in XY:
                if (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1):
                    counter += 1
            if counter >= K:
                comb[counter] += 1


def nCr(n, r):
    if n < r:
        return 0
    if r == 0:
        return 1
    return nCr(n - 1, r - 1) * n // r


ret = 0
for k, v in comb.items():
    ret += v // nCr(k, 2)
print(ret)
