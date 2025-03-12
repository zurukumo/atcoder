N, K = map(int, input().split())
A = [int(i) for i in input().split()]

ok, ng = 0, 10**12 + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    cnt = 0
    for a in A:
        cnt += min(a, mid)
    if cnt <= K:
        ok = mid
    else:
        ng = mid

for i in range(N):
    if A[i] >= ok:
        K -= ok
        A[i] -= ok
    else:
        K -= A[i]
        A[i] = 0

for i in range(N):
    if K > 0 and A[i] > 0:
        A[i] -= 1
        K -= 1

print(*A)
