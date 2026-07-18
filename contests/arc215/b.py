import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]

    C = []
    is_odd = 1
    ok = set()
    ng = set()

    for i, a in enumerate(A):
        if is_odd:
            if a in ok:
                C.append(i)
                ng.add(a)
                is_odd ^= 1
            else:
                ok.add(a)
        else:
            if a in ng:
                C.append(i)
                ok.add(a)
                is_odd ^= 1
            else:
                ng.add(a)

    print(len(C))
    print(*C)
