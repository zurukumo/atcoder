N, x = map(int, input().split())
a = [int(i) for i in input().split()]

ret = float('inf')
dp = [float('inf')] * N
for i in range(N) :
    for j in range(N) :
        dp[(j+i)%N] = min(dp[(j+i)%N], a[j])
    ret = min(ret, sum(dp) + x * i)
print(ret)