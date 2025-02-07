from bisect import bisect_left

N = int(input())
x = [int(i) for i in input().split()]
sorted_x = sorted(x)

mid = N // 2
for i in range(N):
    if bisect_left(sorted_x, x[i]) < mid:
        print(sorted_x[N // 2])
    else:
        print(sorted_x[N // 2 - 1])
