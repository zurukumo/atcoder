import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]

    def bulk_up(i, need):
        if i == 0:
            return

        if A[i - 1] < 2 * need:
            bulk_up(i - 1, 2 * need - A[i - 1])

        if A[i - 1] >= 2 * need:
            A[i] += need
            A[i - 1] -= 2 * need

    for i in range(M - 1, -1, -1):
        if A[i] % N != 0:
            need = N - A[i] % N
            bulk_up(i, need)

    ret = 0
    for i in range(M - 1, -1, -1):
        ret += (1 << i) * (A[i] // N)
        if A[i] % N != 0:
            ret += 1 << i
            break

    print(ret)
