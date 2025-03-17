N, a, b = map(int, input().split())
A = [int(i) for i in input().split()]

ok = 0
ng = 10**9 + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    plus = 0
    minus = 0
    for i in range(N):
        if A[i] > mid:
            minus += (A[i] - mid) // b
        else:
            plus += (mid - A[i] + a - 1) // a
            new_ai = A[i] + (mid - A[i] + a - 1) // a * a
            minus += (new_ai - mid) // b

    if plus <= minus:
        ok = mid
    else:
        ng = mid

print(ok)
