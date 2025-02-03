from sortedcontainers import SortedList

N, K = map(int, input().split())
A = [int(i) - 1 for i in input().split()]


def swap_point(N, K, A):
    sl = SortedList(A)
    idx = [0] * N
    for i in range(N):
        idx[A[i]] = i

    # 未満
    for i in range(N):
        less = sl.bisect_left(A[i])
        if K <= less:
            j = idx[sl[K - 1]]
            return i, j
        K -= less
        sl.remove(A[i])

    # 等しい
    same = N
    if K <= same:
        return 0, 0
    K -= same

    # 超過
    for i in range(N - 1, -1, -1):
        less = sl.bisect_left(A[i])
        more = len(sl) - less
        if K <= more:
            j = idx[sl[less + K - 1]]
            return i, j
        K -= more
        sl.add(A[i])


i, j = swap_point(N, K, A)
print(*[i + 1 for i in A[:i] + A[i : j + 1][::-1] + A[j + 1 :]])
