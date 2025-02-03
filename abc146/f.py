from bisect import bisect_left

N, M = map(int, input().split())
S = input()

reach = []
for i, s in enumerate(S):
    if s == "0":
        reach.append(i)


def solve():
    ret = []
    cur = N
    while cur != 0:
        i = bisect_left(reach, cur - M)
        if reach[i] == cur:
            return [-1]
        ret.append(cur - reach[i])
        cur = reach[i]

    ret.reverse()
    return ret


print(*solve())
