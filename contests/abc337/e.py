N = int(input())

M = len(bin(N - 1)) - 2

print(M)
for i in range(M - 1, -1, -1):
    A = []
    for j in range(1, N + 1):
        if j & (1 << i):
            A.append(j)
    print(len(A), *A)

S = input()

ret = int(S, 2)
if ret == 0:
    print(N)
else:
    print(ret)
