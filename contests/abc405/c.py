N = int(input())
A = [int(i) for i in input().split()]

s = A[::]
for i in range(N - 1):
    s[i + 1] += s[i]

ret = 0
for i in range(N - 1, 0, -1):
    ret += A[i] * s[i - 1]
print(ret)
