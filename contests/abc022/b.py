N = int(input())
A = [int(input()) for _ in range(N)] + [float("inf")]

A.sort()

ret = 0
tmp = 0
ai = A[0]
for aj in A[1:]:
    if ai == aj:
        tmp += 1
    else:
        ret += tmp
        tmp = 0
        ai = aj

print(ret)
