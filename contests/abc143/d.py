from bisect import bisect_left, bisect_right

N = int(input())
L = [int(i) for i in input().split()]

L.sort()
ret = 0
for i in range(N):
    a = L[i]
    for j in range(i + 1, N):
        b = L[j]
        ret += bisect_left(L, a + b) - j - 1
print(ret)
