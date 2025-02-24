N = int(input())
A = [int(i) for i in input().split()]

dp1 = [0] * 10
dp2 = [0] * 100
dp3 = [0] * 1000


def has_seq():
    for i in range(10):
        for j in range(10):
            k = 2 * j - i
            if 0 <= k < 10:
                # print(i * 100 + j * 10 + k)
                if dp3[i * 100 + j * 10 + k] > 0:
                    return True
    return False


ret = N * (N + 1) // 2
l = 0
for r in range(N):
    a = A[r] - 1
    for k in range(100):
        dp3[k * 10 + a] += dp2[k]
    for k in range(10):
        dp2[k * 10 + a] += dp1[k]
    dp1[a] += 1
    while l < r and has_seq():
        a = A[l] - 1
        dp1[a] -= 1
        for k in range(10):
            dp2[a * 10 + k] -= dp1[k]
        for k in range(100):
            dp3[a * 100 + k] -= dp2[k]
        l += 1
    ret -= r - l + 1

print(ret)
