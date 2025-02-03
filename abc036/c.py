from bisect import bisect_left

N = int(input())
a = [int(input()) for _ in range(N)]

b = list(set(a))
b.sort()

for i in range(N) :
    print(bisect_left(b, a[i]))