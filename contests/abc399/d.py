import collections

T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]
    mem = collections.defaultdict(list)
    for i in range(2 * N - 1):
        mem[(A[i], A[i + 1])].append(i)

    ret = 0
    for k, v in mem.items():
        a, b = k
        if len(v) == 2:
            ret += 1
        if a > b:
            continue
        if (b, a) in mem:
            for i in mem[(a, b)]:
                for j in mem[(b, a)]:
                    if abs(i - j) >= 2 and (a, a) not in mem and (b, b) not in mem:
                        ret += 1

    print(ret)
