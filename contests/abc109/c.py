N, X = map(int, input().split())
x = [int(i) for i in input().split()]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


diff = [abs(x[i] - X) for i in range(N)]
ret = diff[0]
for i in range(1, N):
    ret = gcd(ret, diff[i])
print(ret)
