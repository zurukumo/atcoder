import sortedcontainers

N, K = map(int, input().split())
P = [int(i) for i in input().split()]


def solve():
    sc = sortedcontainers.SortedList(P[: K - 1])
    max_k = -1
    max_v = -(10**9)
    for i in range(K - 1, N):
        sc.add(P[i])
        cnt = 0
        while sc and sc[0] == P[i - (K - 1) + cnt]:
            sc.pop(0)
            cnt += 1

        if cnt == K:
            return P

        if i - (K - 1) + cnt > max_v:
            max_k = i - (K - 1)
            max_v = i - (K - 1) + cnt

        if P[i - (K - 1)] in sc:
            sc.remove(P[i - (K - 1)])

    return P[:max_k] + sorted(P[max_k : max_k + K]) + P[max_k + K :]


print(*solve())
