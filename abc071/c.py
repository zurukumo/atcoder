from collections import defaultdict

N = int(input())
A = [int(i) for i in input().split()]

A.sort(reverse=True)
i = 0
ret = 0
while i < N:
    if i + 3 < N and A[i] == A[i + 1] == A[i + 2] == A[i + 3]:
        if ret == 0:
            ret = A[i] * A[i]
        else:
            ret *= A[i]
        break
    elif i + 1 < N and A[i] == A[i + 1]:
        if ret == 0:
            ret = A[i]
            i += 1
        else:
            ret *= A[i]
            break

    i += 1

print(ret)
