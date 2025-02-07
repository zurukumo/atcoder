import bisect

N = int(input())
a = [int(i) for i in input().split()]

a.sort()
visited = [False] * N

ret = 0
for i in range(N):
    if not visited[i]:
        ret += 1

        n = a[i]
        while n <= a[-1]:
            j = bisect.bisect_left(a, n)
            if a[j] == n:
                visited[j] = True
            n *= 2

print(ret)
