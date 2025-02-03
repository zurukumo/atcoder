N = int(input())
A = [int(i) for i in input().split()]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


ret = gcd(A[0], A[1])
for i in range(2, N):
    ret = gcd(ret, A[i])
print(ret)
