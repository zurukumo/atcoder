N, C = map(int, input().split())
T = [int(i) for i in input().split()]

pre_t = -(10**9)
ans = 0
for t in T:
    if t - pre_t >= C:
        ans += 1
        pre_t = t
print(ans)
