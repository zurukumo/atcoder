N = int(input())
P = [int(i) for i in input().split()]

for i in range(N):
    P[i] -= 1


def swap(x, d):
    P[x], P[x + d] = P[x + d], P[x]


def wrong_parity(x):
    if x < 0 or x >= N:
        return False
    return x % 2 != P[x] % 2


ret = []
x = 0
while x < N:
    y = x
    if wrong_parity(y):
        while not wrong_parity(y + 1):
            ret.append(("B", y + 1))
            swap(y, 2)
            y += 2

        swap(y, 1)
        ret.append(("A", y + 1))
    else:
        x += 1

for i in range(N - 1, -1, -1):
    x = P.index(i)
    while x + 2 <= i:
        swap(x, 2)
        ret.append(("B", x + 1))
        x += 2

print(len(ret))
for row in ret:
    print(*row)
