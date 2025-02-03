X, Y = map(int, input().split("/"))


def gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a


g = gcd(X, Y)
X //= g
Y //= g

ret = []
N = ((2 * X // Y) + Y - 1) // Y * Y
if N == 0:
    N += Y

while True:
    M = N * (N + 1) // 2 - X * N // Y
    if M > N:
        break
    ret.append((N, M))
    N += Y

if ret:
    for x, y in ret:
        print(x, y)
else:
    print("Impossible")
