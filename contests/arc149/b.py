import bisect

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

x = [0] * N
for i, a in enumerate(A):
    x[a - 1] = B[i]

lis = [x[0]]
for x in x[1:]:
    if x > lis[-1]:
        lis.append(x)
    else:
        lis[bisect.bisect_left(lis, x)] = x

print(N + len(lis))
